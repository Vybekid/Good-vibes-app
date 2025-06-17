import tkinter as tk
from tkinter import scrolledtext, messagebox

# --- Vasudeva Glyphs Mapping (English -> Vasudeva) ---
# Each English lowercase letter maps to its corresponding Vasudeva glyph.
VASUDEVA_GLYPHS = {
    'a': 'Δ', 'b': '∇', 'c': '○', 'd': '□', 'e': '|', 'f': '—',
    'g': '/', 'h': '\\', 'i': '•', 'j': '⊞', 'k': '⊘', 'l': 'L',
    'm': 'M', 'n': 'N', 'o': '⊗', 'p': 'Π', 'q': 'Ξ', 'r': '⊸',
    's': '∿', 't': '⊥', 'u': '∪', 'v': '∨', 'w': 'W', 'x': '✕',
    'y': 'Y', 'z': 'Z'
}

# --- Reverse Mapping (Vasudeva -> English) ---
# This is created by inverting the VASUDEVA_GLYPHS dictionary.
# It ensures consistency between forward and reverse transliterations.
ENGLISH_LETTERS = {v: k for k, v in VASUDEVA_GLYPHS.items()}

def translate_to_vasudeva(english_text):
    """
    Translates English text to Vasudeva glyphs on a character-by-character basis.
    Non-alphabetic characters (spaces, punctuation, numbers) are preserved.
    Case of English input is ignored (converted to lowercase for mapping).
    """
    vasudeva_output = []
    for char in english_text:
        lower_char = char.lower()
        if lower_char in VASUDEVA_GLYPHS:
            vasudeva_output.append(VASUDEVA_GLYPHS[lower_char])
        else:
            vasudeva_output.append(char) # Preserve non-alphabetic characters
    return "".join(vasudeva_output)

def translate_to_english(vasudeva_text):
    """
    Translates Vasudeva glyphs back to English letters on a character-by-character basis.
    Non-glyph characters are preserved.
    """
    english_output = []
    for char in vasudeva_text:
        if char in ENGLISH_LETTERS:
            english_output.append(ENGLISH_LETTERS[char])
        else:
            english_output.append(char) # Preserve non-glyph characters
    return "".join(english_output)

def perform_english_to_vasudeva_translation():
    """
    Retrieves English text from the input, translates it to Vasudeva,
    and displays the result in the Vasudeva output widget (top-right).
    """
    english_message = english_input_widget.get("1.0", tk.END).strip()
    if not english_message:
        messagebox.showwarning("Input Error", "Please enter some text in English.")
        return

    vasudeva_message = translate_to_vasudeva(english_message)

    output_vasudeva_widget.config(state='normal')
    output_vasudeva_widget.delete("1.0", tk.END)
    output_vasudeva_widget.insert(tk.END, vasudeva_message)
    output_vasudeva_widget.config(state='disabled')

def perform_vasudeva_to_english_translation():
    """
    Retrieves Vasudeva text from the input, translates it to English,
    and displays the result in the English output (from Vasudeva) widget (bottom-left).
    """
    vasudeva_input_message = vasudeva_input_widget_reverse.get("1.0", tk.END).strip()
    if not vasudeva_input_message:
        messagebox.showwarning("Input Error", "Please enter some Vasudeva text to translate back.")
        return

    english_output_message = translate_to_english(vasudeva_input_message)

    output_english_widget_reverse.config(state='normal')
    output_english_widget_reverse.delete("1.0", tk.END)
    output_english_widget_reverse.insert(tk.END, english_output_message)
    output_english_widget_reverse.config(state='disabled')

def copy_vasudeva_output():
    """Copies the Vasudeva output text (top-right) to the clipboard."""
    vasudeva_text = output_vasudeva_widget.get("1.0", tk.END).strip()
    if not vasudeva_text:
        messagebox.showinfo("Copy Info", "No Vasudeva text to copy.")
        return
    root.clipboard_clear()
    root.clipboard_append(vasudeva_text)
    messagebox.showinfo("Copy Info", "Vasudeva text copied to clipboard!")

def copy_english_output_reverse():
    """Copies the English output text (bottom-left) to the clipboard."""
    english_text = output_english_widget_reverse.get("1.0", tk.END).strip()
    if not english_text:
        messagebox.showinfo("Copy Info", "No English text to copy.")
        return
    root.clipboard_clear()
    root.clipboard_append(english_text)
    messagebox.showinfo("Copy Info", "English text copied to clipboard!")

def clear_all_text():
    """Clears all input and output text areas."""
    english_input_widget.delete("1.0", tk.END)
    
    output_vasudeva_widget.config(state='normal')
    output_vasudeva_widget.delete("1.0", tk.END)
    output_vasudeva_widget.config(state='disabled')

    vasudeva_input_widget_reverse.delete("1.0", tk.END)

    output_english_widget_reverse.config(state='normal')
    output_english_widget_reverse.delete("1.0", tk.END)
    output_english_widget_reverse.config(state='disabled')

# --- Tkinter GUI Setup ---
root = tk.Tk()
root.title("Good Vibes Language Translator (Vasudeva)")
root.geometry("800x600") # Adjust initial window size

# Configure grid weights for responsive layout
# Two columns, four main rows (headers, inputs/outputs, buttons, final button)
root.grid_columnconfigure(0, weight=1) # English column
root.grid_columnconfigure(1, weight=1) # My Lang column
root.grid_rowconfigure(1, weight=2) # Top text areas
root.grid_rowconfigure(3, weight=2) # Bottom text areas

# --- Row 0: Headers ---
tk.Label(root, text="English", font=("Arial", 14, "bold")).grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="My Lang (Vasudeva)", font=("Arial", 14, "bold")).grid(row=0, column=1, padx=10, pady=5)

# --- Row 1: Top Translation (English Input -> Vasudeva Output) ---
english_input_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, font=("Arial", 12))
english_input_widget.grid(row=1, column=0, padx=10, pady=5, sticky='nsew')

output_vasudeva_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, 
                                            font=("Arial Unicode MS", 16), state='disabled', bg="#f0f0f0")
output_vasudeva_widget.grid(row=1, column=1, padx=10, pady=5, sticky='nsew')

# --- Row 2: Top Translation Buttons ---
# Button for English -> Vasudeva
translate_e_to_v_btn = tk.Button(root, text="Translate English → Vasudeva", command=perform_english_to_vasudeva_translation,
                                 bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), relief=tk.RAISED)
translate_e_to_v_btn.grid(row=2, column=0, padx=10, pady=5, sticky='ew')

# Copy button for Vasudeva output
copy_vasudeva_btn = tk.Button(root, text="Copy Vasudeva Text", command=copy_vasudeva_output,
                                bg="#2196F3", fg="white", font=("Arial", 10, "bold"), relief=tk.RAISED)
copy_vasudeva_btn.grid(row=2, column=1, padx=10, pady=5, sticky='ew')

# --- Row 3: Separator (or just visual gap) ---
tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN, bg="lightgray").grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

# --- Row 4: Bottom Translation (Vasudeva Input -> English Output) ---
output_english_widget_reverse = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, 
                                                font=("Arial", 12), state='disabled', bg="#f0f0f0")
output_english_widget_reverse.grid(row=4, column=0, padx=10, pady=5, sticky='nsew')

vasudeva_input_widget_reverse = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, 
                                                            font=("Arial Unicode MS", 16)) # Input is not disabled
vasudeva_input_widget_reverse.grid(row=4, column=1, padx=10, pady=5, sticky='nsew')

# --- Row 5: Bottom Translation Buttons ---
# Copy button for English output
copy_english_reverse_btn = tk.Button(root, text="Copy English Text", command=copy_english_output_reverse,
                                    bg="#2196F3", fg="white", font=("Arial", 10, "bold"), relief=tk.RAISED)
copy_english_reverse_btn.grid(row=5, column=0, padx=10, pady=5, sticky='ew')

# Button for Vasudeva -> English
translate_v_to_e_reverse_btn = tk.Button(root, text="Translate Vasudeva → English", command=perform_vasudeva_to_english_translation,
                                     bg="#FFC107", fg="black", font=("Arial", 10, "bold"), relief=tk.RAISED)
translate_v_to_e_reverse_btn.grid(row=5, column=1, padx=10, pady=5, sticky='ew')

# --- Row 6: Global Clear Button ---
clear_all_button = tk.Button(root, text="Clear All Text Areas", command=clear_all_text,
                              bg="#f44336", fg="white", font=("Arial", 10, "bold"), relief=tk.RAISED)
clear_all_button.grid(row=6, column=0, columnspan=2, pady=15, sticky='ew', padx=10)

# Run the application
if __name__ == "__main__":
    root.mainloop()