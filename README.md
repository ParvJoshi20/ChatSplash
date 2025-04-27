
# ChatSplash

ChatSplash is a web-based application designed to provide a visually appealing chat-themed user interface, built with Python (Flask), Tailwind CSS, and vanilla JavaScript.

## Features

- Light and Dark mode UI
- Responsive design with TailwindCSS
- Custom chat mascot and branding
- Smooth transitions and user-friendly layout
- Organized template and static file structure

## Project Structure

```
ChatSplash-main/
│
├── main.py                    # Main Flask application
├── package.json                # Node.js dependencies
├── tailwind.config.js          # Tailwind CSS configuration
├── static/
│   ├── css/
│   │   └── main.css            # Compiled Tailwind CSS
│   ├── js/
│   │   └── script.js           # JavaScript for interactivity
│   ├── images and assets       # Icons, favicon, mascots
│
├── templates/
│   ├── main.html               # Main chat UI
│   ├── light_mode.html         # Light theme version
│   └── dark_mode.html          # Dark theme version
│
└── README.md                   # Project documentation
```

## Installation

1. Clone the repository or download the ZIP.
2. Navigate into the project directory:

   ```bash
   cd ChatSplash-main
   ```

3. Install Python dependencies (if using Flask):

   ```bash
   pip install flask
   ```

4. Install Node.js dependencies (for TailwindCSS):

   ```bash
   npm install
   ```

5. Run Tailwind CLI to watch and build CSS (optional):

   ```bash
   npx tailwindcss -i ./static/input.css -o ./static/css/main.css --watch
   ```

6. Start the Flask app:

   ```bash
   python main.py
   ```

7. Open your browser and navigate to:

   ```
   http://127.0.0.1:5000/
   ```

## Notes

- You can modify the `light_mode.html` and `dark_mode.html` templates to customize the themes.
- All assets (images, favicons) are stored inside the `static/` folder.
- `Untitled Project.aep` is an Adobe After Effects project file, likely for logo or intro animations.
