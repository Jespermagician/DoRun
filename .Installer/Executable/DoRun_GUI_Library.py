import subprocess
import json
import tkinter as tk
from tkinter import ttk
from subprocess import Popen
from abc import abstractmethod
import os
import psutil
import socket
import platform

# ------------------------------------------------------------------------
# DoRunMetadata
# This class contains metadata about the DoRun application.
# ------------------------------------------------------------------------

class DoRunMetadata:
    script_path = os.path.abspath(__file__)
    DoRunRoot = script_path.rsplit(os.path.sep, 3)[0]  # Get the root directory of the project

    DoRunConf = str(str(DoRunRoot) + "\\.Installer\\Executable\\DoRunConf.json")
    DoRunBackendRoot = str( str(DoRunRoot) + "\\Backend\\BackendApp")
    DoRunFrontendRoot = str( str(DoRunRoot) + "\\Frontend\\frontend")
    DoRunLogo = str(str(DoRunRoot) + "\\.Installer\\Executable\\Icons\\DoRun_Logo.png")

# ------------------------------------------------------------------------
# DoRun_Json_Manager
# This class manages the JSON file for the DoRun application.
# Singleton class      
# Usage: 
#   Change
#   - add_key_value("Key", "Value") afterwards save_data(InstanceOfClass._data)
#   - remove_key("Key")             afterwards save_data(InstanceOfClass._data)
#   - modify_value("Key", "Value")  afterwards save_data(InstanceOfClass._data)
#   Get Data
#   - get_key_value("Key") to get the value of a key
#   - get_all_keys() to get all keys
# ------------------------------------------------------------------------
class DoRun_Json_Manager:
    _instance = None

    def __new__(cls, filename):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.filename = filename
            cls._instance._data = cls._instance._load_data()
        return cls._instance

    def _load_data(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error File does not exist: {self.filename} .")
            return {}
        except json.JSONDecodeError:
            print(f"Error decoding the JSON file: {self.filename} .")
            return {}

    def get_data(self):
        return self._data.copy()

    def save_data(self, data):
        try:
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=4)
            self._data = data.copy()
        except IOError as e:
            print(f"When writing to the file {self.filename} an error has occurred - {e}")

    def add_key_value(self, key, value):
        self._data[key] = value

    def remove_key(self, key):
        if key in self._data:
            del self._data[key]

    def modify_value(self, key, value):
        if key in self._data:
            self._data[key] = value
        else:
            print(f"Key '{key}' not found in the configuration.")

    def get_key_value(self, key):
        if key in self._data:
            return self._data[key]
        else:
            return None
    
    def get_all_keys(self):
        return list(self._data.keys())
    
    def update_self(self):
        self._data = self._load_data()

    def append_to_list_or_update(self, key, item, obj_key=None, obj_value=None):
        if key not in self._data:
            self._data[key] = []
        if not isinstance(self._data[key], list):
            print(f"Error: Key '{key}' does not refer to a list.")
            return
        self._data[key].append(item)
        if obj_key is None:
            self._data[key].append(item)
        else:
            self.update_self()
            found_entry = False
            lis = self._data[key]
            if lis:
                for i, existing_item in enumerate(lis):
                    if existing_item[obj_key] == obj_value:
                        del self._data[key][i]  # Remove the existing item with the same key
                        self._data[key].append(item)
                        found_entry = True
                if not found_entry:
                    self._data[key].append(item)
            else:
                self._data[key].append(item)  
    
# ------------------------------------------------------------------------
# Definition of theme-pattern
# This class defines the interface for the theme pattern.
# ------------------------------------------------------------------------
class I_DoRun_Theme:
    @abstractmethod
    def __init__(self):
        self.colour0 = None #Highlight1
        self.colour1 = None #Default
        self.colour2 = None #Darkend1
        self.colour4 = None #Dartkend2
        self.text_colour = None #Default Text Color
        self.progress_bg = None # Background color of the progress bar
        self.progress_light = None # Light color of the progress bar
        self.progress_dark = None # Dark color of the progress bar

# ------------------------------------------------------------------------
#Implementation of the theme-pattern
# ------------------------------------------------------------------------

# Default theme (dark mode)
class DoRun_Theme_Default(I_DoRun_Theme): 
    def __init__(self):
        self.conf = DoRun_Json_Manager(DoRunMetadata.DoRunConf)
        self.colour0 = self.conf.get_key_value("colour_gray_10") #Highlight1
        self.colour1 = self.conf.get_key_value("colour_gray_15") #Default
        self.colour2 = self.conf.get_key_value("colour_gray_30") #Darkend1
        self.colour4 = self.conf.get_key_value("colour_gray_40") #Dartkend2
        self.text_colour = self.conf.get_key_value("colour_white") #Default Text Color
        self.progress_bg = self.conf.get_key_value("progress_bg") # Background color of the progress bar
        self.progress_light = self.conf.get_key_value("progress_light") # Light color of the progress bar
        self.progress_dark = self.conf.get_key_value("progress_dark") # Dark color of the progress bar

# If you hate your life and your eyes
class DoRun_Theme_I_Hate_My_eyes(I_DoRun_Theme):
    def __init__(self):
        self.conf = DoRun_Json_Manager(DoRunMetadata.DoRunConf)
        self.colour0 = self.conf.get_key_value("colour_light_blue") #Highlight1
        self.colour1 = self.conf.get_key_value("colour_white") #Default
        self.colour2 = self.conf.get_key_value("colour_ligth_gray") #Darkend1
        self.colour4 = self.conf.get_key_value("colour_gray") #Dartkend2
        self.text_colour = self.conf.get_key_value("colour_black") #Default Text Color
        self.progress_bg = None # Background color of the progress bar
        self.progress_light = None # Light color of the progress bar
        self.progress_dark = None # Dark color of the progress bar


class DoRun_Frame(tk.Frame):

    Tab_style = "Treeview"

    def __init__(self, root, img_path, Theme : I_DoRun_Theme):

        self.img_path = img_path
        self.DoRunTheme = Theme
        super().__init__(root, bg=self.DoRunTheme.colour1)

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True) # expand=True, damit es sich mit dem Fenster vergrößert
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1) # Gewicht für den oberen Bereich
        self.main_frame.rowconfigure(1, weight=0) # Kein Gewicht für die Fußzeile

    def get_table_style():
    # Gibt den Style für den Treeview zurück
    # Erstelle einen Style-Objekt
        style = ttk.Style()
        style.theme_use("classic")
    # Konfiguriere den Style für den Treeview
        style.configure("Treeview",
                        background="gray15",
                        fieldbackground="gray15",
                        foreground="gray30",
                        relief="solid")
        style.map("Treeview",
                   background=[("selected", "gray30")],
                   foreground=[("selected", "gray40")])
        return DoRun_Frame.Tab_style
    
    def get_columns():
        # Gibt die Spalten für den Treeview zurück
        columns = ["Service", "Name", "Status","", "Note"]
        return columns
    
# ------------------------------------------------------------------------
# DoRun_Service
# This class defines a service used by DoRun.
# Use: information about the service.
# ------------------------------------------------------------------------    
class DoRun_Service:
    def __init__(self, i_name='N/A', name='N/A', display_name='N/A', path='N/A', version='N/A', data_dir='N/A', port='N/A', status='N/A'):
        self.internal_name = i_name
        self.name = name
        self.display_name = display_name
        self.path = path
        self.version = version
        self.data_dir = data_dir
        self.port = port
        self.status = status    

    def to_json_obj(self):
        # Serialisiert das Objekt in ein JSON-Format
        return {
            'internal_name': self.internal_name,
            'name': self.name,
            'display_name': self.display_name,
            'path': self.path,
            'version': self.version,
            'data_dir': self.data_dir,
            'port': self.port,
            'status': self.status
        } 

    def __str__(self):
        return f"Name: {self.name}, Display Name: {self.display_name}, Path: {self.path}, Version: {self.version}, Data Directory: {self.data_dir}, Port: {self.port}, Status: {self.status}"
# ------------------------------------------------------------------------
# DoRun_Service_Manager
# This class manages all services used by DoRun.
# Use: Communication and information about the services.
# ------------------------------------------------------------------------    
class DoRun_Service_Manager:

    def set_service_starttyp(self, service_name, status, note):
        # Setzt den Starttype eines Dienstes / Set the start type of a service
        # Vorsicht bei der Verwendung! / Be careful when using!

        if status not in ["auto", "demand", "disabled"]:
            print(f"Invalid start type: {status}. possible are: auto, demand, disabled.")
            return

        ret = Popen(["sc", "config", service_name, "start=", status])
        if ret.returncode == 0:
            print(f"Start type for {service_name} succesful set {status}")
        else:
            print(f"Error occurred while setting service type for {service_name}: {ret.returncode}")

        pass
    
    def update_service_info(self, internal_name="All"):
        print("Updating service information...")
        #Let the service manager cook
        DoRunServiceManager = DoRun_Service_Manager()
        
        django_service = None
        react_service = None
        found_services = []
        
        if internal_name == "All":
            found_services = DoRunServiceManager.find_service(service_name="postgresql")
            django_service, react_service = DoRunServiceManager.generated_set_dj_re(str(DoRunMetadata.DoRunBackendRoot),str(DoRunMetadata.DoRunFrontendRoot))
                                                                                    
        elif internal_name == "psql":
            found_services = DoRunServiceManager.find_service(service_name="postgresql")

        elif internal_name == "django":
            django_service, react_service = DoRunServiceManager.generated_set_dj_re(str(DoRunMetadata.DoRunBackendRoot), "") #If the path does not exist, the information is not selected

        elif internal_name == "react":
            django_service, react_service = DoRunServiceManager.generated_set_dj_re("",str(DoRunMetadata.DoRunFrontendRoot)) #If the path does not exist, the information is not selected

        for service in found_services:
            path = service.path
            service.version = DoRunServiceManager.get_psql_version(path)    

        count = len(found_services)
        JsonManager = DoRun_Json_Manager(filename=DoRunMetadata.DoRunConf)
        
        # Set service to work with
        if count == 0 and ( internal_name == "psql" or internal_name == "All"):
            print("Please install PostgreSQL befor running this program")
        elif count == 1 and ( internal_name == "psql" or internal_name == "All"):
            found_services[0].internal_name = "psql"
            JsonManager.append_to_list_or_update("services", found_services[0].to_json_obj(),"internal_name", str(found_services[0].internal_name))
            JsonManager.save_data(JsonManager._data)
        elif ( internal_name == "psql" or internal_name == "All"):
            # Ask User which service to use (highlighted the newest one)
            print("Multiple Services found, select the service #Add feature")
        
        if django_service is not None:
            django_service.internal_name = "django"
            JsonManager.append_to_list_or_update("services", django_service.to_json_obj(),"internal_name", str(django_service.internal_name))
            JsonManager.save_data(JsonManager._data)
        
        if react_service is not None:
            react_service.internal_name = "react"
            react_service.name = "React"
            JsonManager.append_to_list_or_update("services", react_service.to_json_obj(),"internal_name", str(react_service.internal_name))
            JsonManager.save_data(JsonManager._data)

        print("Service information updated successfully.")

    def stop_service(self, service_name):
        ret = Popen(["net", "stop", service_name], shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        if ret.returncode == 0 or ret.returncode == None:
            print(f"Service {service_name} stopped successfully.")
        else:
            print(f"Error occurred while stopping service {service_name}: {ret.returncode}")

    def start_service(self, service_name):
        ret = Popen(["net", "start", service_name], shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        if ret.returncode == 0 or ret.returncode == None:
            print(f"Service {service_name} started successfully.")
        else:
            print(f"Error occurred while starting service {service_name}: {ret.returncode}")
# ------------------------------------------------------------------------    
# Return a array [service_name, port, version]
# ------------------------------------------------------------------------    
    def find_service(self, service_name):
        """
            Searches for Windows services that match the specified pattern (in the internal name or display name).
            Returns a list of DoRun_Service objects containing basic details.

            Args:
                service_name_pattern (str): The pattern to look for in the service name or display name.
                This is a substring that should occur in the name or display name.

            Returns:
                list[DoRun_Service]: A list of DoRun_Service objects, each containing the
                basic details of a matching service.
                Returns an empty list if no services are found or an error occurs.
        """
        found_services = []

        try:
            command = f'wmic service where "Caption like \'%{service_name}%\' OR Name like \'%{service_name}%\'" get Name,DisplayName,PathName,State /format:list'

            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True,
                encoding='utf-8',
                errors='replace',
                creationflags=subprocess.CREATE_NO_WINDOW
            )
            output = result.stdout

            current_service_data = {}
            end_of_service = False

            for line in output.splitlines():
                line = line.strip() # Entfernt führende/endende Leerzeichen und Zeilenumbrüche.

                # Parse die Schlüssel-Wert-Paare für jeden Dienst.
                # WMIC /format:list gibt Eigenschaften als "KEY=VALUE" aus.
                if line.startswith("DisplayName="):
                    current_service_data['DisplayName'] = line.split("=", 1)[1]
                elif line.startswith("Name="):
                    current_service_data['Name'] = line.split("=", 1)[1]
                elif line.startswith("PathName="):
                    # Entfernt Anführungszeichen vom Pfad-String, falls vorhanden.
                    current_service_data['PathName'] = line.split("=", 1)[1].strip('"')
                elif line.startswith("State="):
                    current_service_data['State'] = line.split("=", 1)[1]
                    end_of_service = True
                elif not line and current_service_data and end_of_service:
                    end_of_service = False

                    # Erstelle ein DoRun_Service-Objekt mit den gesammelten Daten.
                    found_services.append(
                        DoRun_Service(
                            name=current_service_data.get('Name', 'N/A'),
                            display_name=current_service_data.get('DisplayName', 'N/A'),
                            path=current_service_data.get('PathName', 'N/A'),
                            status=current_service_data.get('State', 'N/A')
                        )
                   )

        except subprocess.CalledProcessError as e:
            # Fängt Fehler ab, die auftreten, wenn der WMIC-Befehl fehlschlägt.
            print(f"Fehler bei der WMIC-Abfrage (Code {e.returncode}): {e}")
            # Versuche, stderr ebenfalls zu dekodieren, um Fehlermeldungen anzuzeigen.
            print(f"Stderr: {e.stderr.decode('utf-8', errors='ignore')}")
            return []
        except FileNotFoundError:
            # Fängt den Fehler ab, wenn 'wmic' nicht im System-PATH gefunden wird.
            print("Der Befehl 'wmic' wurde nicht gefunden. Stellen Sie sicher, dass er im System-PATH ist.")
            return []
        except Exception as e:
            # Fängt alle anderen unerwarteten Fehler ab.
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
            return []

        return found_services
    
    @staticmethod
    def get_psql_version(path):
        try:
            # Assuming the service has a method to get its version
            full_path_string = path
            exe_index = full_path_string.find(".exe")

            if exe_index != -1:
                end_of_path_index = full_path_string.find('"', exe_index)

                if end_of_path_index != -1:
                    executable_path_with_filename = full_path_string[:end_of_path_index]
                else:
                    executable_path_with_filename = full_path_string[:exe_index + len(".exe")]

                last_backslash_index = executable_path_with_filename.rfind("\\")

                if last_backslash_index != -1:
                    desired_path = executable_path_with_filename[:last_backslash_index]

                    result = subprocess.run(
                        ["psql", "--version"],
                        cwd=desired_path,
                        capture_output=True,
                        text=True,
                        check=True, # 'check=True' lässt Python einen Fehler auslösen, wenn der Befehl fehlschlägt
                        env=os.environ.copy(),
                        creationflags=subprocess.CREATE_NO_WINDOW,
                        shell=True
                    )

            return result.stdout.strip()  # Entfernt führende und nachfolgende Leerzeichen
        except Exception as e:
            print(f"Error getting PostgreSQL version: {e}")
            return None
        
# ------------------------------------------------------------------------
#
# From here on the Methods are generated. May contain errors
# Careful with the usage of these methods!
#
# ------------------------------------------------------------------------
    def get_service_status_windows(self, service_name: str) -> str:
        if platform.system() != "Windows":
            return "N/A (Not Windows OS)"
        try:
            cmd = f'sc query "{service_name}" | find "STATE"'
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
            if "RUNNING" in result.stdout.upper():
                return "Running"
            elif "STOPPED" in result.stdout.upper():
                return "Offline"
            elif "PENDING" in result.stdout.upper():
                return "Starting"
            else:
                return "Unknown"
        except subprocess.CalledProcessError:
            return "Service Not Found"
        except Exception as e:
            return f"Error: {e}"

    def is_port_open(self, host: str, port: int, timeout=0.5) -> bool:
        """
        Prüft, ob ein Port auf einem Host geöffnet ist.
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            sock.close()
            return result == 0
        except Exception:
            return False

    def find_python_executable_in_venv(self, base_path: str, venv_name: str = "venv") -> str | None:
        """
        Findet den Pfad zum Python-Interpreter in einem Virtual Environment.
        Sucht im Unterordner 'venv_name' und im übergeordneten Ordner.
        """
        possible_venv_paths = [
            os.path.join(base_path, venv_name), # venv im Projekt-Root
            os.path.join(os.path.dirname(base_path), venv_name) # venv eine Ebene höher (z.B. für Monorepo)
        ]

        for venv_path in possible_venv_paths:
            if platform.system() == "Windows":
                python_exe = os.path.join(venv_path, "Scripts", "python.exe")
            else: # Linux/macOS
                python_exe = os.path.join(venv_path, "bin", "python")
            
            if os.path.exists(python_exe):
                return python_exe
        return None

    def check_process_exists(self, name_keywords: list[str], command_keywords: list[str]) -> bool:
        try:
            for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                try:
                    proc_name = proc.info['name'].lower()
                    proc_cmdline = [arg.lower() for arg in proc.info['cmdline']] if proc.info['cmdline'] else []

                    name_match = any(kw in proc_name for kw in name_keywords)
                    cmd_match = any(any(kw in arg for kw in command_keywords) for arg in proc_cmdline)

                    if name_match or cmd_match:
                        return True # Prozess gefunden
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
            return False
        except Exception as e:
            print(f"Error checking process existence: {e}")
            return False

    # --- Ermittlungsfunktionen für Django ---
    def discover_django_service_info(self,django_project_root: str, django_service_name: str = "DoRunDjangoBackend") -> DoRun_Service:
        """
        Ermittelt Informationen für einen Django-Service und gibt ein DoRun_Service-Objekt zurück.
        :param django_project_root: Absoluter Pfad zum Django-Projekt-Root (wo manage.py ist).
        :param django_service_name: Der gewünschte Name für diesen Django-Service.
        """
        service = DoRun_Service(
            i_name=f"{django_service_name}_internal",
            name=django_service_name,
            display_name=f"{django_service_name} Backend",
            port="8000" # Django Development Server Standardport
        )

        if not os.path.isdir(django_project_root):
            service.status = "Not Found (Root Invalid)"
            return service

        python_exe = self.find_python_executable_in_venv(django_project_root)
        manage_py_path = os.path.join(django_project_root, "manage.py")

        if python_exe and os.path.exists(manage_py_path):
            service.path = python_exe # Der Interpreter, der Django startet

            # 1. Django-Version ermitteln
            try:
                cmd = [python_exe, "-c", "import django; print(django.get_version())"]
                version_result = subprocess.run(cmd, capture_output=True, text=True, check=False, creationflags=subprocess.CREATE_NO_WINDOW)
                if version_result.returncode == 0:
                    service.version = version_result.stdout.strip()
                else:
                    print(f"Warnung: Konnte Django-Version nicht ermitteln. Output: {version_result.stderr.strip()}")
            except Exception as e:
                print(f"Warnung: Fehler beim Ermitteln der Django-Version: {e}")

            # 2. Django-Status ermitteln (via Port-Check und Prozess-Check)
            if service.port.isdigit() and self.is_port_open("127.0.0.1", int(service.port)):
                service.status = "Running"
            else:
                if self.check_process_exists(
                    name_keywords=["python", "gunicorn", "uwsgi"],
                    command_keywords=[f"{os.path.basename(manage_py_path).lower()}", "runserver", "gunicorn", "uwsgi"]
                ):
                    service.status = "Stopped" #Running (Process Found, Port Closed or not 127.0.0.1)
                else:
                    service.status = "Stopped"
            
        else:
            print(f"Warnung: Notwendige Django-Dateien (venv/python.exe oder manage.py) nicht gefunden unter {django_project_root}")
            service.status = "Not Found (Missing Files)"

        return service

    def find_executable_path_for_hint(self, hint_name: str) -> str | None:
        """
        Versucht, den ausführbaren Pfad eines Programms zu finden, basierend auf einem Hinweis (Name).
        """
        if platform.system() != "Windows" or not hint_name:
            return None

        exe_names = _COMMON_WEBSERVER_EXES.get(hint_name.lower())
        if not exe_names:
            exe_names = [f"{hint_name}.exe"] # Fallback: assume .exe

        for exe_name in exe_names:
            # 1. Suche im PATH
            try:
                result = subprocess.run(f"where {exe_name}", shell=True, capture_output=True, text=True, check=False, creationflags=subprocess.CREATE_NO_WINDOW)
                if result.returncode == 0:
                    return result.stdout.strip().split('\n')[0]
            except Exception:
                pass

            # 2. Suche in Standard-Installationspfaden
            for install_path in _DEFAULT_WEBSERVER_INSTALL_PATHS:
                possible_path = os.path.join(install_path, "bin", exe_name)
                if os.path.exists(possible_path):
                    return possible_path
                possible_path = os.path.join(install_path, exe_name)
                if os.path.exists(possible_path):
                    return possible_path
        return None

    def discover_react_service_info(self,react_project_root: str, webserver_name_hint: str = None) -> DoRun_Service:
        """
        Ermittelt Informationen für einen React-Frontend-Service und gibt ein DoRun_Service-Objekt zurück.
        :param react_project_root: Absoluter Pfad zum React-Projekt-Root (wo package.json ist).
        :param webserver_name_hint: Optionaler Hinweis auf den Webserver (z.B. "nginx", "apache2", "node").
        """
        service = DoRun_Service(
            i_name="ReactFrontend_internal",
            name="ReactFrontend",
            display_name="React Frontend Application"
        )

        if not os.path.isdir(react_project_root):
            print(f"Fehler: React-Projekt-Root '{react_project_root}' existiert nicht oder ist kein Verzeichnis.")
            service.status = "Not Found (Root Invalid)"
            return service

        package_json_path = os.path.join(react_project_root, "package.json")
        react_build_path = os.path.join(react_project_root, "build")

        # 1. Version und Name aus package.json ermitteln
        if os.path.exists(package_json_path):
            try:
                with open(package_json_path, 'r', encoding='utf-8') as f:
                    package_data = json.load(f)
                    service.version = package_data.get("version", "N/A")
                    service.name = package_data.get("name", service.name)
                    service.display_name = package_data.get("displayName", f"{service.name} Application")
            except Exception as e:
                print(f"Warnung: Konnte React-Version/Namen aus package.json nicht ermitteln: {e}")
        else:
            print(f"Warnung: package.json nicht gefunden unter {package_json_path}")
            service.version = "N/A (No package.json)"


        # 2. Path ermitteln (nur wenn ein konkretes Executable gefunden wird, sonst N/A belassen)
        detected_host_exe_path = None
        if webserver_name_hint:
            detected_host_exe_path = self.find_executable_path_for_hint(webserver_name_hint)
        
        if detected_host_exe_path:
            service.path = detected_host_exe_path
        # Ansonsten bleibt service.path N/A, wie gewünscht.

        # 3. Port ermitteln (Priorität: Dev-Server, dann Prod-Server)
        if self.is_port_open("127.0.0.1", 3000):
            service.port = "3000"
        elif self.is_port_open("127.0.0.1", 80):
            service.port = "80"
        elif self.is_port_open("127.0.0.1", 443):
            service.port = "443"

        # 4. Status ermitteln
        service_status_from_windows = "N/A (Not a Windows Service)"
        if webserver_name_hint:
            if webserver_name_hint.lower() == "nginx":
                service_status_from_windows = self.get_service_status_windows("nginx")
            elif webserver_name_hint.lower() == "apache2":
                service_status_from_windows = self.get_service_status_windows("Apache2.4")

        if service_status_from_windows not in ["N/A (Not a Windows Service)", "Service Not Found", "Unknown"]:
            service.status = service_status_from_windows
        else:
            is_running_by_port = service.port.isdigit() and self.is_port_open("127.0.0.1", int(service.port))
            is_running_by_process = self.check_process_exists(
                name_keywords=[webserver_name_hint.lower() if webserver_name_hint else "", "node", "npm", "http-server", "serve", "nginx", "httpd"],
                command_keywords=["react-scripts", "start", "serve", "webpack", "npm", "yarn", react_build_path.lower()]
            )

            if is_running_by_port:
                service.status = "Running" # Port open
            elif is_running_by_process:
                service.status = "Stopped" #Process Found but not Port Open
            else:
                service.status = "Stopped"
        
        #if service.status.startswith("Stopped"): # Nur wenn der Status noch "Stopped" ist, Details hinzufügen
        #    if os.path.exists(react_build_path):
        #        if "(Build Ready)" not in service.status: # Vermeide doppelte Anhängsel
        #            service.status += " (Build Ready)"
        #    else:
        #        if "(No Build Found)" not in service.status:
        #            service.status += " (No Build Found)"

        return service


    def generated_set_dj_re(self,django_path :str , react_path :str):

        if not os.path.exists(django_path):
            #print(f"FEHLER: Django-Projekt-Root '{django_path}' existiert nicht. Bitte anpassen.")
            django_service = None
        else:
            django_service = self.discover_django_service_info(django_path, django_service_name="Django")

        if not os.path.exists(react_path):
            #print(f"FEHLER: React-Projekt-Root '{react_path}' existiert nicht. Bitte anpassen.")
            react_service = None
        else:
            react_service = self.discover_react_service_info(react_path)

        return django_service, react_service
    
    # --- Ermittlungsfunktionen für React ---
_COMMON_WEBSERVER_EXES = {
        "nginx": ["nginx.exe"],
        "apache2": ["httpd.exe"],
        "node": ["node.exe"], 
}

_DEFAULT_WEBSERVER_INSTALL_PATHS = [
        "C:\\nginx",
        "C:\\Program Files\\nginx",
        "C:\\Apache24",
        "C:\\Program Files\\Apache Group\\Apache2",
        "C:\\Program Files\\nodejs",
        "C:\\Program Files (x86)\\nodejs",
]

class ProgressBar:
    def __init__(self, parent, theme: I_DoRun_Theme): #Typisierung korrigiert
        self.parent = parent
        self.theme = theme
        self.frame = tk.Frame(parent, bg=self.theme.colour1, height=30)
        
        # Konfiguriere das Grid für den Ladebalken-Frame
        self.frame.columnconfigure(0, weight=1) # Für den Fortschrittsbalken
        self.frame.columnconfigure(1, weight=0) # Für den Text
        
        self.progress_bar = ttk.Progressbar(self.frame, orient="horizontal", length=400, mode="determinate",
                                             style="TProgressbar")
        
        # Stil für den Progressbar anpassen
        style = ttk.Style()
        style.theme_use('default') # Verwende ein Standard-Theme als Basis
        style.configure("TProgressbar",
                        background=self.theme.progress_bg,  # Farbe des Fortschritts
                        troughcolor=self.theme.colour2,      # Farbe des Hintergrunds
                        bordercolor=self.theme.colour1,      # Randfarbe
                        lightcolor=self.theme.progress_light,  # Helle Farbe des Fortschritts
                        darkcolor=self.theme.progress_dark)  # Dunkle Farbe des Fortschritts
        style.map("TProgressbar",
                  background=[('active', self.theme.progress_bg)])

        self.progress_label = tk.Label(self.frame, text="", bg=self.theme.colour1, fg=self.theme.text_colour, font=("Arial", 10))

        self.hide() # Standardmäßig ausgeblendet

    def set_progress(self, percentage: int, text: str = ""):
        """
        Setzt den Fortschritt des Ladebalkens und aktualisiert den Text.
        :param percentage: Der Fortschritt in Prozent (0-100).
        :param text: Optionaler Text, der neben dem Fortschritt angezeigt wird.
        """
        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100.")
        
        self.progress_bar['value'] = percentage
        self.progress_label.config(text=f"{percentage}% {text}")
        self.show() # Sicherstellen, dass der Ladebalken sichtbar ist, wenn er gesetzt wird
        self.parent.update_idletasks() # Wichtig: sofortige GUI-Aktualisierung

    def show(self):
        """Macht den Ladebalken sichtbar."""
        # Platzieren Sie den Frame in der übergeordneten Komponente.
        # Im DoRunController wird dies in row=2 des main_frame sein.
        self.frame.grid(row=2, column=0, sticky=tk.NSEW, pady=(5, 0), padx=5)
        self.progress_bar.grid(row=0, column=0, sticky=tk.EW, padx=(0, 5))
        self.progress_label.grid(row=0, column=1, sticky=tk.E)


    def hide(self):
        """Blendet den Ladebalken aus."""
        self.frame.grid_forget()