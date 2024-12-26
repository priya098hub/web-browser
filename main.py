import tkinter as tk
from tkinter import messagebox
import webbrowser

class WebBrowser:
    def __init__(self):
        # Initialize the main Tkinter window
        self.window = tk.Tk()
        self.window.title("Python Web Browser")

        # Create a frame for the URL entry and buttons
        self.top_frame = tk.Frame(self.window, bg="#f0f0f0")
        self.top_frame.pack(padx=10, pady=10)

        # Create a label and entry for the URL
        self.url_label = tk.Label(self.top_frame, text="URL:", bg="#f0f0f0", fg="#000000")
        self.url_label.pack(side=tk.LEFT)
        self.url_entry = tk.Entry(self.top_frame, width=50, bg="#ffffff", fg="#000000")
        self.url_entry.pack(side=tk.LEFT)

        # Create buttons for searching, bookmarking, and history
        self.search_button = tk.Button(self.top_frame, text="Search", command=self.search_url)
        self.search_button.pack(side=tk.LEFT, padx=10)
        self.bookmark_button = tk.Button(self.top_frame, text="Bookmark", command=self.bookmark_url)
        self.bookmark_button.pack(side=tk.LEFT)
        self.history_button = tk.Button(self.top_frame, text="History", command=self.show_history)
        self.history_button.pack(side=tk.LEFT, padx=10)

        # Create a frame for the browser display
        self.browser_frame = tk.Frame(self.window, bg="#f0f0f0")
        self.browser_frame.pack(padx=10, pady=10)

        # Create a text box for displaying history or messages
        self.browser = tk.Text(self.browser_frame, width=80, height=20, bg="#ffffff", fg="#000000", state=tk.DISABLED)
        self.browser.pack()

    def search_url(self):
        # Retrieve the URL from the entry field
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a URL")
            return
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url

        try:
            # Open the URL in the default web browser
            webbrowser.open(url)
            # Log the search in the browser text box
            self.browser.config(state=tk.NORMAL)
            self.browser.insert(tk.END, f"Searching for {url}...\n")
            self.browser.config(state=tk.DISABLED)
            # Save the URL to history
            with open("history.txt", "a") as file:
                file.write(url + "\n")
        except Exception as e:
            messagebox.showerror("Error", f"Unable to search for {url}: {e}")

    def bookmark_url(self):
        # Retrieve the URL from the entry field
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a URL to bookmark")
            return

        try:
            # Save the URL to a bookmarks file
            with open("bookmarks.txt", "a") as file:
                file.write(url + "\n")
            messagebox.showinfo("Bookmark Added", "URL bookmarked successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Unable to bookmark {url}: {e}")

    def show_history(self):
        try:
            # Read browsing history from the history file
            with open("history.txt", "r") as file:
                history = file.read()
                # Display the history in the text box
                self.browser.config(state=tk.NORMAL)
                self.browser.delete(1.0, tk.END)
                self.browser.insert(tk.END, history)
                self.browser.config(state=tk.DISABLED)
        except FileNotFoundError:
            messagebox.showinfo("No History", "No browsing history found")
        except Exception as e:
            messagebox.showerror("Error", f"Unable to load history: {e}")

    def run(self):
        # Run the Tkinter event loop
        self.window.mainloop()

if __name__ == "__main__":
    browser = WebBrowser()
    browser.run()
