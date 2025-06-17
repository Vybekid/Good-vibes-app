import tkinter as tk
from tkinter import scrolledtext, messagebox

# --- Echelonian Glyphs Mapping (English -> Echelonian) ---
# Each English lowercase letter maps to its corresponding Echelonian glyph.
ECHELONIAN_GLYPHS = {
    'a': 'Δ', 'b': '∇', 'c': '○', 'd': '□', 'e': '|', 'f': '—',
    'g': '/', 'h': '\\', 'i': '•', 'j': '⊞', 'k': '⊘', 'l': 'L',
    'm': 'M', 'n': 'N', 'o': '⊗', 'p': 'Π', 'q': 'Ξ', 'r': '⊸',
    's': '∿', 't': '⊥', 'u': '∪', 'v': '∨', 'w': 'W', 'x': '✕',
    'y': 'Y', 'z': 'Z'
}

# --- Reverse Mapping (Echelonian -> English) ---
# This is created by inverting the ECHELONIAN_GLYPHS dictionary.
# It ensures consistency between forward and reverse translations.
ENGLISH_LETTERS = {v: k for k, v in ECHELONIAN_GLYPHS.items()}

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

def translate_to_english(echelonian_text):
    """
    Translates Echelonian glyphs back to English letters on a character-by-character basis.
    Non-glyph characters are preserved.
    """
    english_output = []
    for char in echelonian_text:
        if char in ENGLISH_LETTERS:
            english_output.append(ENGLISH_LETTERS[char])
        else:
            english_output.append(char) # Preserve non-glyph characters
    return "".join(english_output)

def perform_e_to_e_translation():
    """
    Retrieves English text from the input, translates it to Echelonian,
    and displays the result in the Echelonian output widget.
    """
    english_message = english_input_widget.get("1.0", tk.END).strip()
    if not english_message:
        messagebox.showwarning("Input Error", "Please enter some text in English.")
        return

    echelonian_message = translate_to_echelonian(english_message)

    output_echelonian_widget.config(state='normal')
    output_echelonian_widget.delete("1.0", tk.END)
    output_echelonian_widget.insert(tk.END, echelonian_message)
    output_echelonian_widget.config(state='disabled')

def perform_e_to_e_reverse_translation():
    """
    Retrieves Echelonian text from the input, translates it to English,
    and displays the result in the English output (from Echelonian) widget.
    """
    echelonian_input_message = echelonian_input_widget_reverse.get("1.0", tk.END).strip()
    if not echelonian_input_message:
        messagebox.showwarning("Input Error", "Please enter some Echelonian text to translate back.")
        return

    english_output_message = translate_to_english(echelonian_input_message)

    output_english_widget_reverse.config(state='normal')
    output_english_widget_reverse.delete("1.0", tk.END)
    output_english_widget_reverse.insert(tk.END, english_output_message)
    output_english_widget_reverse.config(state='disabled')

def copy_echelonian_text():
    """
    Copies the Echelonian output text to the clipboard.
    """
    echelonian_text = output_echelonian_widget.get("1.0", tk.END).strip()
    if not echelonian_text:
        messagebox.showinfo("Copy Info", "No Echelonian text to copy.")
        return
    
    root.clipboard_clear()
    root.clipboard_append(echelonian_text)
    messagebox.showinfo("Copy Info", "Echelonian text copied to clipboard!")

def copy_english_reverse_text():
    """
    Copies the English output text (from Echelonian) to the clipboard.
    """
    english_text = output_english_widget_reverse.get("1.0", tk.END).strip()
    if not english_text:
        messagebox.showinfo("Copy Info", "No English text to copy.")
        return
    
    root.clipboard_clear()
    root.clipboard_append(english_text)
    messagebox.showinfo("Copy Info", "English text copied to clipboard!")

def clear_all_text():
    """
    Clears all input and output text areas.
    """
    english_input_widget.delete("1.0", tk.END)
    
    output_echelonian_widget.config(state='normal')
    output_echelonian_widget.delete("1.0", tk.END)
    output_echelonian_widget.config(state='disabled')

    echelonian_input_widget_reverse.delete("1.0", tk.END)

    output_english_widget_reverse.config(state='normal')
    output_english_widget_reverse.delete("1.0", tk.END)
    output_english_widget_reverse.config(state='disabled')

# --- Tkinter GUI Setup ---
root = tk.Tk()
root.title("Good Vibes Language Translator (Echelonian Transliteration)")
root.geometry("750x800") # Adjust initial window size to accommodate new sections

# Configure grid weights for responsive layout
root.grid_rowconfigure(1, weight=1) # English input row
root.grid_rowconfigure(3, weight=1) # Echelonian output row
root.grid_rowconfigure(6, weight=1) # Echelonian input reverse row
root.grid_rowconfigure(8, weight=1) # English output reverse row
root.grid_columnconfigure(0, weight=1) 
root.grid_columnconfigure(1, weight=1)

# --- Section 1: English to Echelonian ---
english_label = tk.Label(root, text="English Input:")
english_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')

english_input_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=8, font=("Arial", 12))
english_input_widget.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

e_to_e_button_frame = tk.Frame(root)
e_to_e_button_frame.grid(row=2, column=0, columnspan=2, pady=5)

translate_button = tk.Button(e_to_e_button_frame, text="Translate English to Echelonian", command=perform_e_to_e_translation,
                             bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), relief=tk.RAISED)
translate_button.pack(side=tk.LEFT, padx=10)

echelonian_output_label = tk.Label(root, text="Echelonian Output (Good Vibes Language):")
echelonian_output_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')

# Using a font that typically supports a wide range of Unicode characters for the glyphs
output_echelonian_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=8, 
                                            font=("Arial Unicode MS", 16), state='disabled', bg="#f0f0f0")
output_echelonian_widget.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

copy_echelonian_btn = tk.Button(e_to_e_button_frame, text="Copy Echelonian Text", command=copy_echelonian_text,
                        bg="#2196F3", fg="white", font=("Arial", 10, "bold"), relief=tk.RAISED)
copy_echelonian_btn.pack(side=tk.LEFT, padx=10)

# --- Separator ---
separator = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN, bg="gray")
separator.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='ew')


# --- Section 2: Echelonian to English ---
echelonian_input_label_reverse = tk.Label(root, text="Echelonian Input:")
echelonian_input_label_reverse.grid(row=6, column=0, padx=10, pady=5, sticky='w')

echelonian_input_widget_reverse = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=8, 
                                                            font=("Arial Unicode MS", 16)) # Input is not disabled
echelonian_input_widget_reverse.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

e_to_e_reverse_button_frame = tk.Frame(root)
e_to_e_reverse_button_frame.grid(row=8, column=0, columnspan=2, pady=5)

reverse_translate_button = tk.Button(e_to_e_reverse_button_frame, text="Translate Echelonian to English", command=perform_e_to_e_reverse_translation,
                                     bg="#FFC107", fg="black", font=("Arial", 10, "bold"), relief=tk.RAISED)
reverse_translate_button.pack(side=tk.LEFT, padx=10)

english_output_label_reverse = tk.Label(root, text="English Output (from Echelonian):")
english_output_label_reverse.grid(row=9, column=0, padx=10, pady=5, sticky='w')

output_english_widget_reverse = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=8, 
                                                font=("Arial", 12), state='disabled', bg="#f0f0f0")
output_english_widget_reverse.grid(row=10, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

copy_english_reverse_btn = tk.Button(e_to_e_reverse_button_frame, text="Copy English Text", command=copy_english_reverse_text,
                                    bg="#2196F3", fg="white", font=("Arial", 10, "bold"), relief=tk.RAISED)
copy_english_reverse_btn.pack(side=tk.LEFT, padx=10)

# --- Global Clear Button ---
clear_all_button = tk.Button(root, text="Clear All Text", command=clear_all_text,
                              bg="#f44336", fg="white", font=("Arial", 10, "bold"), relief=tk.RAISED)
clear_all_button.grid(row=11, column=0, columnspan=2, pady=15)

# Run the application
if __name__ == "__main__":
    root.mainloop()