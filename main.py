import tkinter as tk
from tkinter import scrolledtext, messagebox

# --- Echelonian Glyphs Mapping ---
# Each English lowercase letter maps to its corresponding Echelonian glyph.
# Non-alphabetic characters will be passed through as they are.
ECHELONIAN_GLYPHS = {
    'a': 'Δ', 'b': '∇', 'c': '○', 'd': '□', 'e': '|', 'f': '—',
    'g': '/', 'h': '\\', 'i': '•', 'j': '⊞', 'k': '⊘', 'l': 'L',
    'm': 'M', 'n': 'N', 'o': '⊗', 'p': 'Π', 'q': 'Ξ', 'r': '⊸',
    's': '∿', 't': '⊥', 'u': '∪', 'v': '∨', 'w': 'W', 'x': '✕',
    'y': 'Y', 'z': 'Z'
}

def translate_to_echelonian(english_text):
    """
    Translates English text to Echelonian glyphs on a character-by-character basis.
    Non-alphabetic characters (spaces, punctuation, numbers) are preserved.
    Case of English input is ignored (converted to lowercase for mapping).
    """
    echelonian_output = []
    for char in english_text:
        lower_char = char.lower()
        if lower_char in ECHELONIAN_GLYPHS:
            echelonian_output.append(ECHELONIAN_GLYPHS[lower_char])
        else:
            echelonian_output.append(char) # Preserve non-alphabetic characters
    return "".join(echelonian_output)

def perform_translation():
    """
    Retrieves English text from the input, translates it, and displays the result.
    """
    english_message = input_text_widget.get("1.0", tk.END).strip() # Get all text from start to end
    if not english_message:
        messagebox.showwarning("Input Error", "Please enter some text in English.")
        return

    echelonian_message = translate_to_echelonian(english_message)

    # Update the Echelonian output text area
    output_text_widget.config(state='normal') # Enable editing temporarily to insert text
    output_text_widget.delete("1.0", tk.END) # Clear previous content
    output_text_widget.insert(tk.END, echelonian_message) # Insert new content
    output_text_widget.config(state='disabled') # Make it read-only again

def copy_echelonian_text():
    """
    Copies the Echelonian output text to the clipboard.
    """
    echelonian_text = output_text_widget.get("1.0", tk.END).strip()
    if not echelonian_text:
        messagebox.showinfo("Copy Info", "No Echelonian text to copy.")
        return
    
    root.clipboard_clear()
    root.clipboard_append(echelonian_text)
    messagebox.showinfo("Copy Info", "Echelonian text copied to clipboard!")

def clear_all_text():
    """
    Clears both input and output text areas.
    """
    input_text_widget.delete("1.0", tk.END)
    output_text_widget.config(state='normal')
    output_text_widget.delete("1.0", tk.END)
    output_text_widget.config(state='disabled')

# --- Tkinter GUI Setup ---
root = tk.Tk()
root.title("Good Vibes Language Translator (Echelonian Transliteration)")
root.geometry("700x500") # Set initial window size

# Configure grid weights for responsive layout
root.grid_rowconfigure(1, weight=1) # English input row
root.grid_rowconfigure(3, weight=1) # Echelonian output row
root.grid_columnconfigure(0, weight=1) # Left column for labels
root.grid_columnconfigure(1, weight=1) # Right column for text areas and buttons

# --- English Input Section ---
english_label = tk.Label(root, text="English Input:")
english_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')

input_text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, font=("Arial", 12))
input_text_widget.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

# --- Buttons Section ---
button_frame = tk.Frame(root)
button_frame.grid(row=2, column=0, columnspan=2, pady=10)

translate_button = tk.Button(button_frame, text="Translate to Echelonian", command=perform_translation,
                             bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), relief=tk.RAISED)
translate_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(button_frame, text="Clear All", command=clear_all_text,
                         bg="#f44336", fg="white", font=("Arial", 10, "bold"), relief=tk.RAISED)
clear_button.pack(side=tk.LEFT, padx=10)

# --- Echelonian Output Section ---
echelonian_label = tk.Label(root, text="Echelonian Output (Good Vibes Language):")
echelonian_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')

# Using a font that typically supports a wide range of Unicode characters for the glyphs
output_text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, 
                                            font=("Arial Unicode MS", 16), state='disabled', bg="#f0f0f0")
output_text_widget.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

copy_button = tk.Button(root, text="Copy Echelonian Text", command=copy_echelonian_text,
                        bg="#2196F3", fg="white", font=("Arial", 10, "bold"), relief=tk.RAISED)
copy_button.grid(row=5, column=0, columnspan=2, pady=5)


# Run the application
if __name__ == "__main__":
    root.mainloop()