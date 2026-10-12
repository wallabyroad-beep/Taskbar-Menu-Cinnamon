# Taskbar Menu

![Taskbar Menu icon](src/taskbar-menu@cornelishaferkamp/icon.png)

## Project overview

Taskbar Menu creates custom application menus in the Cinnamon panel. Add separate menus for work, graphics, games, or any other collection of installed applications. Each applet instance stores its own settings.

Version: **0.1.0** · Applet UUID: `taskbar-menu@cornelishaferkamp`

## Features

- Multiple independent applet instances, each with its own application selection.
- Search installed applications by name, description, or desktop file ID.
- Browse the application categories supplied by Cinnamon.
- Select or deselect multiple applications before applying changes.
- See the selection count and a summary grouped by category.
- Set an individual menu name and icon for each instance.
- Choose **Icon only**, **Text only**, or **Icon and text** for the applet in the panel.
- Move the application selection dialog by dragging its title bar.
- Launch an application from the menu; missing applications appear as disabled entries.

**The three display modes affect only the applet in the Cinnamon panel. Applications inside the opened menu are displayed with an icon and a name.** Search and category browsing are available in the application selection dialog.

## Screenshots

The original promotional image is preserved in [docs/original-overview.png](docs/original-overview.png). It shows an earlier application selection interface and is provided as historical artwork, not as a screenshot of the current dialog. The current dialog has a draggable title bar and a selection summary. No new screenshot has been fabricated.

## Requirements

- Linux Mint with the Cinnamon desktop (the metadata declares Cinnamon **6.6**).
- A normal user account; administrator privileges are not required for applet installation.
- Git for the Git installation method, or an archive manager for ZIP installation.

The applet uses Cinnamon's built-in libraries. There is no build step or additional runtime package to install. Other Cinnamon versions and desktop environments are not verified.

## Installation

### Install with Git

Install Git through Linux Mint's Software Manager if necessary. Open a terminal in a directory where you keep downloaded projects:

```sh
git clone https://github.com/wallabyroad-beep/Taskbar-Menu-Cinnamon.git
cd Taskbar-Menu-Cinnamon
mkdir -p "$HOME/.local/share/cinnamon/applets"
cp -a src/taskbar-menu@cornelishaferkamp "$HOME/.local/share/cinnamon/applets/"
```

The resulting path must be:

```text
~/.local/share/cinnamon/applets/taskbar-menu@cornelishaferkamp/applet.js
```

### Install with a ZIP download

On the GitHub repository page, choose **Code → Download ZIP**, then extract the archive. Open a terminal inside the extracted project folder and run the same `mkdir` and `cp` commands shown above.

If a release provides `taskbar-menu-0.1.0.zip`, extract it instead. That installable archive contains the UUID folder directly. Open a terminal inside its extracted folder and run:

```sh
mkdir -p "$HOME/.local/share/cinnamon/applets"
cp -a taskbar-menu@cornelishaferkamp "$HOME/.local/share/cinnamon/applets/"
```

### Activate the applet and add more instances

1. Open **System Settings → Applets**, or right-click the panel and choose **Applets**.
2. On the **Manage** tab, select **Taskbar Menu** and click the **+** button to add it to the panel.
3. Repeat the **+** action to add another independent instance. The metadata does not impose an instance limit.
4. Configure each instance separately using its panel context menu.

If Taskbar Menu does not appear after copying the files, log out and log back in, then reopen Applets. Panel edit mode can be used to move instances to suitable positions.

## How to use

1. Right-click an instance in the panel and choose **Configure**.
2. On **General**, set the menu name, panel display mode, and icon.
3. On **Applications**, click **Manage applications…**.
4. Browse a category or enter a search term. Searching covers all categories.
5. Click application rows to select or deselect them. Review the count and summary.
6. Click **Apply** to save changes, or **Cancel** to discard them. Apply is enabled when the selection changes.
7. Click the panel applet to open its menu, then click an application to launch it.

Drag the title bar of the selection dialog to move it around the screen.

## Configuration

| Setting | Purpose |
| --- | --- |
| Menu name | Label displayed in text modes; defaults to `New Menu`. |
| Panel display | Icon only, text only, or icon and text; defaults to both. |
| Icon | A theme icon or an image file; defaults to `folder-symbolic`. |
| Applications | The installed applications selected for this instance. |

The supplied green project icon is retained as `icon.png`. To use it as a panel icon, select the installed file at `~/.local/share/cinnamon/applets/taskbar-menu@cornelishaferkamp/icon.png` in the icon chooser. The default panel icon is the theme's folder icon.

Cinnamon stores settings separately for each instance. Its settings files are normally under `~/.config/cinnamon/spices/taskbar-menu@cornelishaferkamp/`. Avoid editing them while the applet is running.

## Updating

From your Git checkout:

```sh
cd Taskbar-Menu-Cinnamon
git pull --ff-only
mkdir -p "$HOME/.local/share/cinnamon/applets"
cp -a src/taskbar-menu@cornelishaferkamp/. "$HOME/.local/share/cinnamon/applets/taskbar-menu@cornelishaferkamp/"
```

For ZIP installations, download and extract the newer project archive and run the same copy command from inside that folder. With an installable release archive, copy from `taskbar-menu@cornelishaferkamp/.` instead of `src/taskbar-menu@cornelishaferkamp/.`.

Log out and back in to load the updated code. Copying the applet files does not overwrite Cinnamon's per-instance settings. Back up the settings directory before updating if you want to retain a separate copy.

## Uninstallation

First remove **every** Taskbar Menu instance using its panel context menu or the Applets manager. Then delete the installed applet:

```sh
rm -rf -- "$HOME/.local/share/cinnamon/applets/taskbar-menu@cornelishaferkamp"
```

To completely remove saved settings as well, run the following optional command. It permanently removes the configuration of all Taskbar Menu instances:

```sh
rm -rf -- "$HOME/.config/cinnamon/spices/taskbar-menu@cornelishaferkamp"
```

The downloaded Git checkout or extracted ZIP folder can then be removed through your file manager. Installed applications are unaffected.

## Known limitations

- Compatibility is declared for Cinnamon 6.6; other versions have not been verified here.
- Only applications exposed through Cinnamon's application menu are available for selection. Hidden applications are excluded.
- The launcher menu is a flat list. Custom submenus, separators, manual reordering, arbitrary commands, websites, and configuration import/export are not implemented.
- Application selection is sorted alphabetically when saved; there is no manual ordering control.
- Applet interface strings are in English; translated application names and category names come from Cinnamon.
- The selection dialog uses fixed dimensions and may be inconvenient on small screens.
- Uninstalled applications can leave disabled entries in an existing menu. Open the manager and apply a changed selection to refresh the saved list.
- The original promotional image does not represent the current selection dialog exactly.

## License

Copyright © 2026 Cornelis Haferkamp.

The existing source headers license Taskbar Menu under the **GNU General Public License, version 3 only (GPL-3.0-only)**. The full text is included in [LICENSE](LICENSE).

The applet integrates with Cinnamon's APIs. No separately attributed third-party code components were identified in the supplied project files; this does not independently establish the origin of every line of code or artwork.
