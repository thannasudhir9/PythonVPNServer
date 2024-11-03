# SecureVPN Application

This repository contains two versions of the SecureVPN application:
1. A modern web application built with React
2. A desktop application built with Python

## Web Version (React)

### Features
- Beautiful, modern UI with Tailwind CSS
- Real-time connection status monitoring
- Server load visualization
- Data transfer tracking
- Responsive design
- Interactive server selection

### Prerequisites
- Node.js 16+ installed
- npm or yarn package manager

### Installation & Running (Web Version)

1. Clone the repository
2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The application will open automatically in your default browser.

### Building for Production
```bash
npm run build
```

The built files will be in the `dist` directory.

## Desktop Version (Python)

### Features
- Native desktop interface
- Real-time connection monitoring
- Server management
- Data transfer simulation
- Cross-platform compatibility

### Prerequisites
- Python 3.6+
- Tkinter (usually comes with Python)

### Installation & Running (Desktop Version)

#### Windows

1. Ensure Python is installed:
   - Download Python from [python.org](https://python.org)
   - During installation, check "Add Python to PATH"
   - Ensure to check "tcl/tk and IDLE" during installation

2. Run the application:
```cmd
python main.py
```

#### Linux

1. Install Python and Tkinter:

Ubuntu/Debian:
```bash
sudo apt update
sudo apt install python3 python3-tk
```

Fedora:
```bash
sudo dnf install python3 python3-tkinter
```

Arch Linux:
```bash
sudo pacman -S python python-tk
```

2. Run the application:
```bash
python3 main.py
```

## Application Structure

### Web Version
```
src/
├── components/
│   ├── ConnectionStatus.tsx   # Connection monitoring component
│   └── ServerList.tsx        # Server listing and selection
├── types.ts                  # TypeScript interfaces
└── App.tsx                   # Main application component
```

### Python Version
```
.
├── main.py          # Main application file
└── requirements.txt # Python dependencies
```

## Usage

1. Launch the application (web or desktop version)
2. Browse the available VPN servers
3. Click "Connect" on your chosen server
4. Monitor your connection status
5. Click "Disconnect" to end the VPN session

## Technical Details

### Web Version
- Built with React 18
- Styled with Tailwind CSS
- Uses Lucide icons
- TypeScript for type safety
- Modular component architecture

### Desktop Version
- Built with Python 3
- Uses Tkinter for GUI
- Object-oriented design
- Real-time updates using Tkinter's event loop

## Important Notes

This is a demonstration application and does not implement actual VPN functionality. In a production environment, you would need to:

1. Implement actual VPN protocols (OpenVPN/WireGuard)
2. Add proper authentication
3. Handle encryption and security
4. Manage network interfaces
5. Implement proper error handling
6. Add server-side infrastructure
7. Include proper security measures

## Development

### Web Version
- Use `npm run dev` for development
- ESLint is configured for code quality
- TypeScript ensures type safety
- Components are modular and reusable

### Desktop Version
- Python code follows PEP 8 style guide
- Object-oriented design for maintainability
- Tkinter provides native GUI elements
- Simulated data for demonstration