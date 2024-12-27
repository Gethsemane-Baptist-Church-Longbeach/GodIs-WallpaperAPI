<h1 align="center">📱 <a href="https://github.com/Gethsemane-Baptist-Church-Longbeach/GodIs-WallpaperAPI">GodIs-WallpaperAPI</a></h1>

<h4 align="center">🎨 A Flask-based API to serve faith-based wallpapers for various devices and months.</h4>

<p align="center">
<a href="https://twitter.com/PinoyITSolution"><img src="https://img.shields.io/twitter/follow/PinoyITSolution?style=social"></a>
<a href="https://github.com/ronknight?tab=followers"><img src="https://img.shields.io/github/followers/ronknight?style=social"></a>
<a href="https://github.com/ronknight/ronknight/stargazers"><img src="https://img.shields.io/github/stars/BEPb/BEPb.svg?logo=github"></a>
<a href="https://github.com/ronknight/ronknight/network/members"><img src="https://img.shields.io/github/forks/BEPb/BEPb.svg?color=blue&logo=github"></a>
<a href="https://youtube.com/@PinoyITSolution"><img src="https://img.shields.io/youtube/channel/subscribers/UCeoETAlg3skyMcQPqr97omg"></a>
<a href="https://github.com/Gethsemane-Baptist-Church-Longbeach/GodIs-WallpaperAPI/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/Gethsemane-Baptist-Church-Longbeach/GodIs-WallpaperAPI/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="#"><img src="https://img.shields.io/badge/Made%20with-Love-1f425f.svg"></a>
<a href="https://github.com/ronknight"><img src="https://img.shields.io/badge/Made%20with%20%F0%9F%A4%8D%20by%20-%20Ronknight%20-%20red"></a>
</p>

---

## 📖 Table of Contents
<p align="center">
  <a href="#project-overview">Project Overview</a> •
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#api-endpoints">API Endpoints</a> •
  <a href="#contribution">Contribution</a> •
  <a href="#license">License</a>
</p>

---

## 📜 Project Overview
The **GodIs-WallpaperAPI** is a Flask-based API designed to serve inspirational, faith-based wallpapers. Wallpapers are organized by months and optimized for various devices such as desktops, laptops, tablets, and watches. The API supports fetching random wallpapers, retrieving specific wallpapers by month and device, and providing a list of available months.

---

## ✨ Features
- **Faith-Based Wallpapers**: Organizes wallpapers by months for easy access.
- **Device-Specific Support**: Serves wallpapers tailored to specific devices:
  - Desktop
  - Laptop
  - Tablet
  - Watch
- **Random Image Support**: Fetch a random wallpaper from any month and device.
- **Custom Requests**: Retrieve wallpapers for a specific month and device.
- **JSON Responses**: Provides structured responses for programmatic access.

---

## 🚀 Installation

### Prerequisites
- **Python 3.8+**
- **Flask** (install via `pip`)
- Basic understanding of setting up a Flask application.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Gethsemane-Baptist-Church-Longbeach/GodIs-WallpaperAPI.git
   cd GodIs-WallpaperAPI
   ```
2. Install dependencies:
   ```bash
   pip install flask
   ```
3. Create the required directory structure:
   - Ensure the directory `static/wallpapers` exists.
   - Add subdirectories for each month (e.g., `January`, `February`, etc.).
   - Place device-specific wallpapers (`desktop.jpg`, `tablet.png`, etc.) in the respective month folders.

4. Run the Flask app:
   ```bash
   python app.py
   ```

5. The app will start on `http://127.0.0.1:5000`.

---

## 🧑‍💻 Usage

### Start the API Server
Run the app as described in the installation steps.

### Available Wallpaper Files
Place your wallpapers in the `static/wallpapers/<month>/` directory with filenames corresponding to supported devices (e.g., `desktop.jpg`, `tablet.png`, etc.).

### Example Request
- **Fetch a list of available months**:
  ```bash
  curl http://127.0.0.1:5000/months
  ```
  **Response**:
  ```json
  ["January", "February", "March", ..., "December"]
  ```

- **Fetch a random wallpaper for a specific device**:
  ```bash
  curl http://127.0.0.1:5000/random-desktop
  ```
  This returns the wallpaper file for a randomly chosen month.

- **Fetch a wallpaper for a specific month and device**:
  ```bash
  curl http://127.0.0.1:5000/March/tablet
  ```
  If a wallpaper exists for March and tablet, it will be served. Otherwise, a `404` error is returned.

- **Fetch a random wallpaper from any month and device**:
  ```bash
  curl http://127.0.0.1:5000/random
  ```

---

## 🔗 API Endpoints

| Endpoint                  | Method | Description                                     |
|---------------------------|--------|-------------------------------------------------|
| `/months`                 | GET    | Retrieve a list of available months.           |
| `/random-<device>`        | GET    | Fetch a random wallpaper for a specific device.|
| `/<month>/<device>`       | GET    | Fetch a wallpaper for a specific month/device. |
| `/random`                 | GET    | Fetch a random wallpaper (any month/device).   |

### Supported Devices
- `desktop`
- `laptop`
- `tablet`
- `watch`

### Supported Months
- January, February, March, ..., December

---

## 🤝 Contribution
We welcome contributions to improve the API or add new features:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/my-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add my feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/my-feature
   ```
5. Open a Pull Request on GitHub.

---

## 📝 License
This project is licensed under the **MIT License**. See the [LICENSE](https://github.com/Gethsemane-Baptist-Church-Longbeach/GodIs-WallpaperAPI/blob/master/LICENSE) file for details.

---

## ⚠️ Disclaimer
This project serves images stored locally in the `static/wallpapers` directory. Ensure that all images comply with copyright regulations before distributing them.
