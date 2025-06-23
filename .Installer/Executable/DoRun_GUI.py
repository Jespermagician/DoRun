import tkinter as tk
from tkinter import ttk
import os
import DoRun_GUI_Library as GUI

title = "DoRun Controller GUI"
version = "1.0.0.Beta"

WindowName = title + " " + version
WindowSize = "700x350"

class DoRunController(GUI.DoRun_Frame):
    def __init__(self, root, img_path, DoRunTheme : GUI.I_DoRun_Theme):
        #Application extension
        self.DoRunTheme = DoRunTheme

        self.root = root
        #General configuration for DoRun GUI
        super().__init__(root, img_path=img_path, Theme=DoRunTheme)  # Initialisierung der Elternklasse
        self.icon_cache = {}  # Cache für geladene Icons

        # Initialisiere den Ladebalken
        self.progress_bar_widget = GUI.ProgressBar(self.main_frame, self.DoRunTheme)

        self.overlay_frame = tk.Frame(root, bg='grey', cursor="wait")

        self.overlay_toplevel = tk.Toplevel(self.root)
        self.overlay_toplevel.withdraw()
        self.overlay_toplevel.overrideredirect(True)
        self.overlay_toplevel.attributes('-alpha', 0.5)
        self.overlay_toplevel.attributes('-topmost', True)
        self.overlay_toplevel.config(bg='grey')

        tk.Label(self.overlay_toplevel, text="", bg='grey', cursor="wait").pack(expand=True, fill=tk.BOTH)

        self.root.bind("<Configure>", self._on_root_configure)

    def _on_root_configure(self, event=None):
        if self.overlay_toplevel.winfo_exists() and self.overlay_toplevel.state() == "normal":
            x = self.root.winfo_x()
            y = self.root.winfo_y()
            width = self.root.winfo_width()
            height = self.root.winfo_height()
            self.overlay_toplevel.geometry(f"{width}x{height}+{x}+{y}")


    def load_main_widgets(self):
        self.create_page_frame()
        #self.create_menu()
        #self.main_frame.bind("<Configure>", self.update_wraplength)
        
        # Beispiel: Ladebalken nach dem Laden der Widgets anzeigen

    def create_page_frame(self):
        self.page_frame = tk.Frame(self.main_frame, bg=self.DoRunTheme.colour1)
        self.page_frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.page_frame.columnconfigure(0, weight=1) # Spalte für Service
        self.page_frame.columnconfigure(1, weight=1) # Spalte für Status
        self.page_frame.columnconfigure(2, weight=1) # Spalte für Port
        self.page_frame.columnconfigure(3, weight=1) # Spalte für Notes

        # Titel-Label (zentriert über dem Text)
        title_label = tk.Label(self.page_frame, text="DoRun Server Controller", font=("Arial", 16), bg=self.DoRunTheme.colour1, fg=self.DoRunTheme.text_colour, anchor="center")
        title_label.grid(row=0, column=0, columnspan=4, padx=0, pady=(0, 0), sticky="n")

        self.create_header_row()
        self.set_rows()
        self.create_global_control_buttons_grid()

    def set_rows(self):
        JsonLoader = GUI.DoRun_Json_Manager(filename=GUI.DoRunMetadata.DoRunConf)
        #Load Json
        Services = JsonLoader.get_key_value("services")

        for service in Services:
            internal_name = service['internal_name']
            status = service['status']
            sname = service['name']

            match internal_name:
                case "psql":
                    self.create_service_row(service_name="Database:", sname=sname, status=status, note="", row=4, internal_name=internal_name)
                case "react":
                    self.create_service_row(service_name="Frontend:", sname=sname, status=status, note="", row=2, internal_name=internal_name)
                case "django":
                    self.create_service_row(service_name="Backend:", sname=sname, status=status, note="", row=3, internal_name=internal_name)
        

    def create_header_row(self):
        # Titel
        col = GUI.DoRun_Frame.get_columns()

        for i, column in enumerate(col):
            t1 = tk.Label(self.page_frame, text=column, font=("Arial", 13), bg=self.DoRunTheme.colour1, fg=self.DoRunTheme.text_colour, anchor="w")
            t1.grid(row=1, column=i, padx=(5, 0), pady=(10, 0), sticky="w") # 'ew' für horizontale Ausdehnung

    def create_service_row(self, service_name, status, note, row, internal_name="", sname=""):

        # Icon basierend auf dem Status
        icon_name = ""
        if status == "Stopped" or status == "Stop Pending":
            icon_name = "Icon_OnHold.png"
        elif status == "Running" or status == "Start Pending":
            icon_name = "Icon_Running.png"
        elif status == "Error":
            icon_name = "Icon_Error.png"
        elif status == "Starting":
            icon_name = "Icon_Starting.png"

        icon_img = self.load_icon(icon_name)
        icon_label = tk.Label(self.page_frame, image=icon_img, bg=self.DoRunTheme.colour1)
        icon_label.image = icon_img  # Keep a reference!
        icon_label.grid(row=row, column=3, padx=(0, 0), pady=(0, 0), sticky="w")

        #Service Name
        SN = tk.Label(self.page_frame, text=service_name, font=("Arial", 12), bg=self.DoRunTheme.colour1, fg=self.DoRunTheme.text_colour, anchor="w")
        SN.grid(row=row, column=0, padx=(5, 0), pady=(5, 0), sticky="ew")

        #Service Name / Real Name
        SN = tk.Label(self.page_frame, text=sname, font=("Arial", 12), bg=self.DoRunTheme.colour1, fg=self.DoRunTheme.text_colour, anchor="w")
        SN.grid(row=row, column=1, padx=(5, 0), pady=(5, 0), sticky="ew")

        #Status
        ST = tk.Label(self.page_frame, text=status, font=("Arial", 12), bg=self.DoRunTheme.colour1, fg=self.DoRunTheme.text_colour, anchor="w")
        ST.grid(row=row, column=2, padx=(5, 0), pady=(5, 0), sticky="ew")

        #Note
        NO_entry = tk.Entry(self.page_frame, font=("Arial", 12), bg=self.DoRunTheme.colour1, fg=self.DoRunTheme.text_colour)
        NO_entry.insert(0, note)  # Insert the initial note
        NO_entry.grid(row=row, column=4, padx=(5, 0), pady=(5, 0), sticky="ew")

        # Buttons mit Platzhalter-Aktionen
        Start = tk.Button(self.page_frame, text="Start", font=("Arial", 12), bg=self.DoRunTheme.colour1, fg=self.DoRunTheme.text_colour,
                             command=lambda: self.start_service(internal_name))
        Start.grid(row=row, column=5, padx=(5, 0), pady=(10, 0), sticky="ew")

        Stop = tk.Button(self.page_frame, text="Stop", font=("Arial", 12), bg=self.DoRunTheme.colour1, fg=self.DoRunTheme.text_colour,
                             command=lambda: self.stop_service(internal_name))
        Stop.grid(row=row, column=6, padx=(5, 0), pady=(10, 0), sticky="e")

        # Function comes in a later Version
        #Reset = tk.Button(self.page_frame,text="Start" , font=("Arial", 12), bg=self.DoRunTheme.colour1, fg=self.DoRunTheme.text_colour)
        #Reset.grid(row=row, column=4, padx=(5, 0), pady=(5, 0), sticky="ew")

    def create_global_control_buttons_grid(self):
        # Erstelle ein neues Frame für die Buttons
        self.global_buttons_frame = tk.Frame(self.main_frame, bg=self.DoRunTheme.colour1)
        # Platziere dieses Frame in der nächsten Zeile des main_frame (row=1, da page_frame in row=0 ist)
        self.global_buttons_frame.grid(row=3, column=0, sticky=tk.NSEW, pady=(10, 0)) # Etwas Abstand oben

        # Konfiguriere die Spalten dieses neuen Frames
        self.global_buttons_frame.columnconfigure(0, weight=1) # Leere Spalte links für Abstand
        self.global_buttons_frame.columnconfigure(1, weight=1) # Für Start All
        self.global_buttons_frame.columnconfigure(2, weight=1) # Für Stop All
        self.global_buttons_frame.columnconfigure(3, weight=1) # Für Update Status
        self.global_buttons_frame.columnconfigure(4, weight=1) # Leere Spalte rechts für Abstand

        # Start All Button
        start_all_btn = tk.Button(self.global_buttons_frame, text="Start All", font=("Arial", 12), bg=self.DoRunTheme.colour1, fg=self.DoRunTheme.text_colour,
                                     command=lambda: self.start_service("All"))
        start_all_btn.grid(row=0, column=1, padx=(5, 0), pady=(0, 0), sticky="ew")

        # Stop All Button
        stop_all_btn = tk.Button(self.global_buttons_frame, text="Stop All", font=("Arial", 12), bg=self.DoRunTheme.colour1, fg=self.DoRunTheme.text_colour,
                                  command=lambda: self.stop_service("All"))
        stop_all_btn.grid(row=0, column=2, padx=(5, 0), pady=(0, 0), sticky="ew")

        # Update Status Button
        update_status_btn = tk.Button(self.global_buttons_frame, text="Update Status", font=("Arial", 12), bg=self.DoRunTheme.colour1, fg=self.DoRunTheme.text_colour,
                                          command=lambda: self.update_service_info())
        update_status_btn.grid(row=0, column=3, padx=(5, 0), pady=(0, 0), sticky="ew")


    def update_service_info(self):
        self.disable_interaction("Update status...") # Sperrt die Interaktion und zeigt den Ladebalken an
        ServiceManager = GUI.DoRun_Service_Manager()
        ServiceManager.update_service_info()
        self.set_rows()
        self.enable_interaction("Updated status...") # Sperrt die Interaktion und zeigt den Ladebalken an


    def start_service(self, internal_name):
        self.disable_interaction(f"Starting service: {internal_name}") # Sperrt die Interaktion und zeigt den Ladebalken an
        ServiceManager = GUI.DoRun_Service_Manager()
        ConfigManager = GUI.DoRun_Json_Manager(filename=GUI.DoRunMetadata.DoRunConf)

        match internal_name:
            case "All":
                Services = ConfigManager.get_key_value("services")
                for service in Services:
                    if service['internal_name'] == "psql":
                        name = service['name']
                        break
                ServiceManager.start_service(name)

            case "psql":
                Services = ConfigManager.get_key_value("services")
                for service in Services:
                    if service['internal_name'] == "psql":
                        name = service['name']
                        break
                ServiceManager.start_service(name)

            case "django":
                print("React service start not implemented yet")
            case "react":
                print("React service start not implemented yet")

        ServiceManager.update_service_info(internal_name)
        self.set_rows()
        self.enable_interaction(f"{internal_name} started!") # Gibt die Interaktion wieder frei und blendet den Ladebalken aus


    def stop_service(self, internal_name):
        self.disable_interaction(f"Stopping service: {internal_name}") # Sperrt die Interaktion und zeigt den Ladebalken an
        ServiceManager = GUI.DoRun_Service_Manager()
        ConfigManager = GUI.DoRun_Json_Manager(filename=GUI.DoRunMetadata.DoRunConf)

        match internal_name:
            case "All":
                Services = ConfigManager.get_key_value("services")
                for service in Services:
                    if service['internal_name'] == "psql":
                        name = service['name']
                        break
                ServiceManager.stop_service(name)

            case "psql":
                Services = ConfigManager.get_key_value("services")
                for service in Services:
                    if service['internal_name'] == "psql":
                        name = service['name']
                        break
                ServiceManager.stop_service(name)

            case "django":
                print("React service stop not implemented yet")
            case "react":
                print("React service stop not implemented yet")

        ServiceManager.update_service_info(internal_name)
        self.set_rows()
        self.enable_interaction(f"{internal_name} stopped!") # Gibt die Interaktion wieder frei und blendet den Ladebalken aus

    def load_icon(self, icon_name, subsample_x=8, subsample_y=8):
        """Lädt ein Icon, verkleinert es und speichert es im Cache."""
        if icon_name not in self.icon_cache:
            icon_path = os.path.join(os.path.dirname(__file__), "Icons", icon_name)
            try:
                img = tk.PhotoImage(file=icon_path)
                self.icon_cache[icon_name] = img.subsample(subsample_x, subsample_y)
            except tk.TclError as e:
                print(f"Fehler beim Laden des Icons '{icon_name}': {e}")
                return None
        return self.icon_cache[icon_name]

    def disable_interaction(self, message="Please wait..."):
        """Sperrt alle Benutzereingaben und zeigt den Ladebalken an."""
        self.overlay_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.progress_bar_widget.set_progress(0, message)
        self.update_idletasks() # Wichtig, um die GUI sofort zu aktualisieren

    def enable_interaction(self, message="Finshed!"):
        self.overlay_frame.place_forget()
        self.progress_bar_widget.set_progress(100, message) # Setzt auf 100% vor dem Ausblenden
        self.after(2000, self.progress_bar_widget.hide) # Blendet nach kurzer Verzögerung aus

def main():
    #Set DoRun theme for frame
    DoRunTheme = GUI.DoRun_Theme_Default() #GUI.DoRun_Theme_I_Hate_My_eyes()

    DoRunLogo = GUI.DoRunMetadata.DoRunLogo

    #Global configuration
    root = tk.Tk()
    root.title(WindowName)
    root.geometry(WindowSize)
    root.resizable(True,True)
    root.config(bg=DoRunTheme.colour1)

    #load icon
    icon = tk.PhotoImage(file=DoRunLogo)
    root.iconphoto(True, icon)

    #Create main window
    DoRunInstance = DoRunController(root, DoRunLogo, DoRunTheme)

    #Let the service manager cook
    DoRunServiceManager = GUI.DoRun_Service_Manager()
    DoRunServiceManager.update_service_info()

    #Start GUI
    DoRunInstance.load_main_widgets()

    root.mainloop()

if __name__ == "__main__":
    main()