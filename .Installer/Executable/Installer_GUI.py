import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import ImageTk, Image
from subprocess import Popen, PIPE
import os
import sys
import threading # Import für das Threading


import DoRun_GUI_Library as GUI

title = "DoRun SetUp GUI"
version = "1.0.0.Beta"

WindowName = title + " " + version
WindowSize = "700x350"

# Custom stdout/stderr writer to redirect print statements to a Tkinter Text widget
class ConsoleRedirector:
    def __init__(self, text_widget, do_print_to_console=True): # do_print_to_console standardmäßig auf True setzen
        self.text_widget = text_widget
        self.do_print_to_console = do_print_to_console
        self.stdout = sys.__stdout__ # Keep a reference to the original stdout

    def write(self, message):
        # Wenn do_print_to_console True ist, wird auch in die Systemkonsole geschrieben.
        # Dies ist nützlich für Debugging, um zu sehen, was in der realen Konsole passiert.
        if self.do_print_to_console:
            self.stdout.write(message)
        
        # Sicherstellen, dass die GUI-Operationen im Hauptthread ausgeführt werden
        # Dies ist entscheidend, wenn print() von einem anderen Thread aufgerufen wird (z.B. im Batch-Leseprozess)
        def _insert_message():
            self.text_widget.config(state=tk.NORMAL)
            self.text_widget.insert(tk.END, message)
            self.text_widget.see(tk.END) # Scroll to the end
            self.text_widget.config(state=tk.DISABLED)
            # self.text_widget.update_idletasks() # Entweder hier oder am Ende der Schleife im Leseprozess

        # root.after ist die sichere Methode, um GUI-Operationen von einem Nicht-GUI-Thread aus aufzurufen
        if self.text_widget.winfo_exists(): # Nur aktualisieren, wenn das Widget noch existiert
            self.text_widget.after(0, _insert_message)


    def flush(self):
        # This method is required for file-like objects
        if self.do_print_to_console:
            self.stdout.flush()

class DoRunInstaller(GUI.DoRun_Frame):
    def __init__(self, root, img_path, DoRunTheme: GUI.I_DoRun_Theme):
        # Application extension
        self.installationsverzeichnis_var = tk.StringVar(value="C:\\Program Files\\DoRun")
        self.DoRunTheme = DoRunTheme
        self.project_name = "DoRun"
        self.project_venv_name = "DoRun_Venv"
        self.project_dir_name = "DoRun"
        self.Debug = False  # Set to True for debugging output

        # General configuration for DoRun GUI
        super().__init__(root, img_path=img_path, Theme=DoRunTheme)

        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.rowconfigure(1, weight=0)
        self.main_frame.rowconfigure(2, weight=0)
        self.main_frame.rowconfigure(3, weight=0)
        self.main_frame.columnconfigure(0, weight=1)

        self.load_main_widgets()

        # Redirect stdout and stderr *after* GUI is fully set up,
        # using the self.Info Text widget for console output.
        sys.stdout = ConsoleRedirector(self.Info, do_print_to_console=True)
        sys.stderr = ConsoleRedirector(self.Info, do_print_to_console=True)


    def load_main_widgets(self):
        self.create_page_frame()
        self.create_status_and_progress_widgets()
        self.create_menu()

        # TEST: Überprüfen, ob der Redirector funktioniert. Dieser Text sollte sofort erscheinen.
        print('Redirector test: This message should appear in the Info box.\n')
        print('Initializing DoRun SetUp GUI...\n') # Added newline for better formatting
        self.master.bind("<Configure>", self.update_wraplength)


    def create_page_frame(self):
        self.page_frame = tk.Frame(self.main_frame, bg=self.DoRunTheme.colour1)
        self.page_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=0, pady=0)

        self.page_frame.columnconfigure(0, weight=0)
        self.page_frame.columnconfigure(1, weight=1)
        self.page_frame.rowconfigure(0, weight=1)
        self.page_frame.rowconfigure(1, weight=0)

        self.img_tk = None

        try:
            print (f"Image path: {self.img_path}")
            if os.path.exists(self.img_path):
                pil_img = Image.open(self.img_path)
                resized_img = pil_img.resize((100, 100), Image.Resampling.LANCZOS)
                self.img_tk = ImageTk.PhotoImage(resized_img)
            else:
                print(f"Warning: Image file not found at '{self.img_path}'. Image will not be displayed.")
        except Exception as e:
            print(f"Error loading image: {e}")

        if self.img_tk:
            image_label = tk.Label(self.page_frame, image=self.img_tk, bg=self.DoRunTheme.colour1)
            image_label.grid(row=0, column=0, padx=20, pady=20, sticky="nw")

        title_label = tk.Label(self.page_frame, text="DoRun SetUp", font=("Arial", 16), bg=self.DoRunTheme.colour1, fg=self.DoRunTheme.text_colour, anchor="center")
        title_label.grid(row=0, column=1, padx=20, pady=(20, 0), sticky="n")

        self.text_label = tk.Label(
            self.page_frame,
            text="This is an auto SetUp Program for the software DoRun. To start the download, select an installation path (if the path does not exist, the directory will be created) and then press 'Continue'.",
            font=("Arial", 10),
            bg=self.DoRunTheme.colour1,
            fg=self.DoRunTheme.text_colour,
            justify="left",
            wraplength=1
        )
        self.text_label.grid(row=0, column=1, padx=20, pady=(60, 0), sticky="nw")

        lower_frame = tk.Frame(self.page_frame, bg=self.DoRunTheme.colour1)
        lower_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=20, pady=10)
        lower_frame.columnconfigure(0, weight=0)
        lower_frame.columnconfigure(1, weight=1)
        lower_frame.columnconfigure(2, weight=0)

        label_verzeichnis = tk.Label(lower_frame, text="Installation Path:", bg=self.DoRunTheme.colour1, fg=self.DoRunTheme.text_colour, anchor="w")
        label_verzeichnis.grid(row=0, column=0, padx=0, pady=0, sticky="w")

        entry_verzeichnis = tk.Entry(lower_frame, textvariable=self.installationsverzeichnis_var, bg=self.DoRunTheme.colour2, fg=self.DoRunTheme.text_colour, insertbackground=self.DoRunTheme.text_colour)
        entry_verzeichnis.grid(row=0, column=1, padx=5, pady=0, sticky="ew")

        button_waehlen = tk.Button(
            lower_frame,
            text="/",
            width=5,
            command=self.waehle_installationsverzeichnis,
            bg=self.DoRunTheme.colour2,
            fg=self.DoRunTheme.text_colour,
            activebackground=self.DoRunTheme.colour4,
            activeforeground=self.DoRunTheme.text_colour
        )
        button_waehlen.grid(row=0, column=2, padx=5, pady=0, sticky="e")

    def create_status_and_progress_widgets(self):
        # This is the status label *above* the progress bar
        self.status_var = tk.StringVar(value="Ready to install...")
        self.status_label = ttk.Label(self.main_frame, textvariable=self.status_var, background=self.DoRunTheme.colour1, foreground=self.DoRunTheme.text_colour)
        self.status_label.grid(row=1, column=0, sticky="w", padx=20, pady=4)

        style = ttk.Style()
        style.theme_use('default')
        style.configure("Custom.Horizontal.TProgressbar",
                        background=self.DoRunTheme.colour2,
                        troughcolor=self.DoRunTheme.colour0,
                        bordercolor=self.DoRunTheme.text_colour,
                        lightcolor=self.DoRunTheme.text_colour,
                        darkcolor=self.DoRunTheme.colour0,
                        thickness=10)

        self.progress_bar = ttk.Progressbar(self.main_frame, orient="horizontal", length=400, mode="determinate", style="Custom.Horizontal.TProgressbar")
        self.progress_bar.grid(row=2, column=0, sticky="ew", padx=20, pady=4)

    def create_menu(self):
        self.menu_frame = tk.Frame(self.main_frame, bg=self.DoRunTheme.colour1)
        self.menu_frame.grid(row=3, column=0, sticky="ew", padx=20, pady=10)
        
        # Neu: Konfigurieren Sie die Spalten des menu_frame
        self.menu_frame.columnconfigure(0, weight=1) # Für das Info-Textfeld (soll sich ausdehnen)
        self.menu_frame.columnconfigure(1, weight=0) # Für die Scrollbar
        self.menu_frame.columnconfigure(2, weight=0) # Für den Button-Frame

        self.Info = tk.Text(self.menu_frame, height=3, bg=self.DoRunTheme.colour0, fg=self.DoRunTheme.text_colour, wrap=tk.WORD, borderwidth=0, highlightthickness=0)
        self.Info.config(state=tk.DISABLED) # Start as disabled
        self.Info.grid(row=0, column=0, sticky="ew", padx=(0,0)) # Info in Spalte 0

        if self.Debug == False:
            self.Info.grid_remove()

        # Add a scrollbar to the Info Text widget
        self.Info_scrollbar = tk.Scrollbar(self.menu_frame, command=self.Info.yview)
        # Scrollbar in Spalte 1, direkt neben dem Textfeld
        self.Info_scrollbar.grid(row=0, column=1, sticky="ns") 
        self.Info.config(yscrollcommand=self.Info_scrollbar.set)

        if self.Debug == False:
            self.Info_scrollbar.grid_remove()
        
        button_frame = tk.Frame(self.menu_frame, bg=self.DoRunTheme.colour1)
        # Button frame jetzt in Spalte 2
        button_frame.grid(row=0, column=2, sticky="e") 

        # Deactivate the Back button permanently
        self.back_button = tk.Button(button_frame, text="Back", width=10, command=self.back_action, bg=self.DoRunTheme.colour2, fg=self.DoRunTheme.text_colour, activebackground=self.DoRunTheme.colour4, activeforeground=self.DoRunTheme.text_colour, state=tk.DISABLED)
        self.back_button.pack(side="left", padx=5, pady=0)

        self.continue_button = tk.Button(button_frame, text="Continue", width=10, command=self.continue_action, bg="forest green", fg=self.DoRunTheme.text_colour, activebackground="green", activeforeground=self.DoRunTheme.text_colour)
        self.continue_button.pack(side="left", padx=5, pady=0)

        self.quit_button = tk.Button(button_frame, text="Quit", width=10, command=self.quit_program, bg=self.DoRunTheme.colour2, fg=self.DoRunTheme.text_colour, activebackground=self.DoRunTheme.colour4, activeforeground=self.DoRunTheme.text_colour)
        self.quit_button.pack(side="left", padx=5, pady=0)

    def quit_program(self):
        self.master.destroy()

    def back_action(self):
        print("Back button clicked (Function disabled).")
        # messagebox.showinfo("Info", "Back function not yet implemented.") # This message will now also print to Info field

    def update_status(self, message, progress=0):
        # This updates the status label (above the progress bar)
        self.status_var.set(message)
        self.progress_bar['value'] = progress
        self.master.update_idletasks()

    def continue_action(self):
        install_base_dir = self.installationsverzeichnis_var.get()

        if not install_base_dir:
            messagebox.showerror("Error", "Please select an installation path.")
            return

        final_install_dir = os.path.join(install_base_dir, self.project_dir_name)

        if not messagebox.askyesno("Start Installation?", f"Would you like to install '{self.project_name}' in '{final_install_dir}'?"):
            return

        self.update_status("Installation started...", 0)
        self.back_button.config(state=tk.DISABLED) # Ensure it stays disabled
        self.continue_button.config(state=tk.DISABLED)
        self.quit_button.config(state=tk.DISABLED)

        # WICHTIG: Sicherstellen, dass die Batch-Datei im richtigen Pfad ist.
        installer_bat_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "DoRun_Installer.bat")

        print(f"DEBUG: Checking for installer at: {installer_bat_path}") # Debugging-Ausgabe
        if not os.path.exists(installer_bat_path):
            print(f"ERROR: Installer batch file not found at: {installer_bat_path}") # Debugging-Ausgabe
            messagebox.showerror("Error", f"Installer batch file not found:\n{installer_bat_path}\nPlease ensure 'DoRun_Installer.bat' is in the 'Executable' directory next to the GUI file.")
            self.update_status("Installation failed.", 0)
            self.back_button.config(state=tk.DISABLED) 
            self.continue_button.config(state=tk.NORMAL)
            self.quit_button.config(state=tk.NORMAL)
            return

        try:
            process = Popen([installer_bat_path, final_install_dir],
                            cwd=os.path.dirname(installer_bat_path),
                            stdout=PIPE, stderr=PIPE, shell=True,
                            creationflags=0x08000000 
                           )

            def read_output_lines():
                # Read line by line from stdout and stderr
                for line in iter(process.stdout.readline, b''):
                    decoded_line = line.decode('utf-8', errors='ignore').strip()
                    if decoded_line:
                        print(f"BATCH_OUT: {decoded_line}")
                        # Aktualisiere den Fortschrittsbalken und Status-Label
                        current_progress = self.progress_bar['value'] + 5
                        if current_progress > 95: current_progress = 95
                        self.update_status(f"Installation: {decoded_line}", current_progress)
                
                for line in iter(process.stderr.readline, b''):
                    decoded_line = line.decode('utf-8', errors='ignore').strip()
                    if decoded_line:
                        print(f"BATCH_ERR: {decoded_line}")
                        self.update_status(f"ERROR: {decoded_line}", self.progress_bar['value'])

            # Starten Sie das Lesen des Outputs in einem separaten Thread,
            # um die GUI nicht zu blockieren.
            output_reader_thread = threading.Thread(target=read_output_lines, daemon=True)
            output_reader_thread.start()

            # Überprüfen Sie regelmäßig, ob der Batch-Prozess beendet wurde.
            def check_process_status():
                if process.poll() is None: # Prozess läuft noch
                    self.master.after(100, check_process_status)
                else: # Prozess beendet
                    print("DEBUG: Batch process finished.")
                    # Stellen Sie sicher, dass alle verbleibenden Ausgaben gelesen wurden
                    remaining_stdout = process.stdout.read().decode('utf-8', errors='ignore').strip()
                    remaining_stderr = process.stderr.read().decode('utf-8', errors='ignore').strip()

                    if remaining_stdout:
                        print(f"BATCH_OUT (final): {remaining_stdout}")
                    if remaining_stderr:
                        print(f"BATCH_ERR (final): {remaining_stderr}")

                    retcode = process.returncode

                    if retcode == 0:
                        print(f'\nInstallation of {self.project_name} successful!')
                        self.update_status("Installation complete.", 100)
                        messagebox.showinfo("Success", f"'{self.project_name}' has been successfully installed in:\n{final_install_dir}")
                    else:
                        error_detail = remaining_stderr if remaining_stderr else "No specific error message from batch."
                        if not error_detail and remaining_stdout:
                            error_detail = "Batch output (if any):\n" + remaining_stdout
                        
                        print(f'\nInstallation failed with return code: {retcode}')
                        self.update_status("Installation failed.", 0)
                        messagebox.showerror("Installation Error", f"Installation of '{self.project_name}' failed.\n\nReturn Code: {retcode}\n\nDetails:\n{error_detail}")
                    
                    self.back_button.config(state=tk.DISABLED) # Ensure it stays disabled
                    self.continue_button.config(state=tk.NORMAL)
                    self.quit_button.config(state=tk.NORMAL)

            self.master.after(50, check_process_status) # Start checking process status

        except FileNotFoundError:
            print(f"ERROR: Installer batch file not found in try block: '{installer_bat_path}'") # Debugging-Ausgabe
            messagebox.showerror("Error", f"The installer could not be found: '{installer_bat_path}'\nPlease check the path.")
            self.update_status("Installation failed.", 0)
            self.back_button.config(state=tk.DISABLED)
            self.continue_button.config(state=tk.NORMAL)
            self.quit_button.config(state=tk.NORMAL)
        except Exception as e:
            print(f"ERROR: An unexpected error occurred during batch execution: {e}") # Debugging-Ausgabe
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
            self.update_status("Installation failed.", 0)
            self.back_button.config(state=tk.DISABLED)
            self.continue_button.config(state=tk.NORMAL)
            self.quit_button.config(state=tk.NORMAL)

    def waehle_installationsverzeichnis(self):
        selected_directory = filedialog.askdirectory(
            title="Choose installation path",
            initialdir=self.installationsverzeichnis_var.get()
        )
        if selected_directory:
            self.installationsverzeichnis_var.set(selected_directory)
            print(f"Selected installation directory: {selected_directory}")

    def update_wraplength(self, event=None):
        if self.text_label.winfo_exists() and self.page_frame.winfo_exists():
            try:
                bbox = self.page_frame.grid_bbox(row=0, column=1)
                if bbox is not None and bbox[2] > 0:
                    calculated_wraplength = max(1, bbox[2] - 40)
                    self.text_label.config(wraplength=calculated_wraplength)
                else:
                    fallback_wraplength = self.main_frame.winfo_width() - 160
                    self.text_label.config(wraplength=max(1, fallback_wraplength))
            except Exception as e:
                print(f"Error during wraplength calculation: {e}")
                self.text_label.config(wraplength=max(1, self.main_frame.winfo_width() - 160))

def main():
    DoRunTheme = GUI.DoRun_Theme_Default()

    root = tk.Tk()
    root.title(WindowName)
    root.geometry(WindowSize)
    root.resizable(False, False)
    root.config(bg=DoRunTheme.colour1)

    img_path = GUI.DoRunMetadata.DoRunLogo

    try:
        icon = tk.PhotoImage(file=img_path)
        root.iconphoto(True, icon)
    except tk.TclError as e:
        print(f"Error loading window icon '{img_path}': {e}")
        print("Please ensure the image file exists and is in PNG format.")
    except Exception as e:
        print(f"An unexpected error occurred while loading the window icon: {e}")

    DoRunInstance = DoRunInstaller(root, img_path, DoRunTheme)

    root.update_idletasks()
    DoRunInstance.update_wraplength()

    root.mainloop()

if __name__ == "__main__":
    main()