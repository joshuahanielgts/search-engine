import tkinter as tk
from tkinter import ttk
import webbrowser
from exa_py import Exa

# Initialize Exa
exa = Exa('YOUR_EXA_API_KEY')

# Handle search
def perform_search():
    query = search_var.get()
    if not query.strip():
        return

    for widget in results_frame.winfo_children():
        widget.destroy()

    response = exa.search(
        query,
        num_results=10,
        type='keyword',
        include_domains=['https://www.tiktok.com'],
    )

    if not response.results:
        ttk.Label(results_frame, text="No results found.", style="Result.TLabel").pack(pady=10)
        return

    for result in response.results:
        title = result.title or "No Title"
        url = result.url or "No URL"

        def open_url(link=url):
            webbrowser.open(link)

        ttk.Label(results_frame, text=title, style="Title.TLabel").pack(anchor='w', padx=10)
        ttk.Button(results_frame, text=url, command=open_url, style="Link.TButton").pack(anchor='w', padx=20, pady=(0, 10))


# --- GUI Setup ---
root = tk.Tk()
root.title("Exa Search Engine - TikTok Only")
root.geometry("700x500")
root.configure(bg="#1a1a1a")

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#1a1a1a", foreground="white", font=("Segoe UI", 11))
style.configure("Result.TLabel", foreground="lightgray", font=("Segoe UI", 10))
style.configure("Title.TLabel", foreground="#00ffcc", font=("Segoe UI", 12, "bold"))
style.configure("Link.TButton", foreground="#0099ff", background="#333333", font=("Segoe UI", 10), borderwidth=0)
style.map("Link.TButton", background=[("active", "#444444")], foreground=[("active", "white")])

# Top Frame
top_frame = ttk.Frame(root)
top_frame.pack(pady=20)

search_var = tk.StringVar()
search_entry = ttk.Entry(top_frame, textvariable=search_var, width=50, font=("Segoe UI", 12))
search_entry.pack(side=tk.LEFT, padx=(0, 10))

search_btn = ttk.Button(top_frame, text="Search", command=perform_search)
search_btn.pack(side=tk.LEFT)

# Results Frame with Scrollbar
canvas = tk.Canvas(root, bg="#1a1a1a", highlightthickness=0)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
results_frame = ttk.Frame(canvas)

results_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=results_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True, padx=20, pady=10)
scrollbar.pack(side="right", fill="y")

root.mainloop()
