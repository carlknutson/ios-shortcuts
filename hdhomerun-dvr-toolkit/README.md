## HDHomeRun DVR Tookit

#### Download [link](https://www.icloud.com/shortcuts/f7ce4b37fc8d47579667b798d190a8c2)

iOS shortcut for managing HDHomeRun DVR
- mass delete recordings
- retrieve dvr storage details

## Pre-requites
1. [a-Shell](https://apps.apple.com/us/app/a-shell/id1473805438) installed and configured on iPhone
    1. Open a-Shell, and execute the following command: `curl hdhomerun.local`
    1. You should receive a pop-up that states `"a-Shell" would like to find and connect to devices on your local network ...",` select `Allow`
    1. If you do not see the pop-up, or you mistakenly selected `Don't Allow`, you can access this toggle setting from iOS `Settings` app -> `a-Shell` -> `Local Network`
    1. If the `Local Network` toggle is enabled, but you are still having issues with connecting to `hdhomerun.local`, restart the phone and try connecting again, trust me :)
1. iPhone is connected to same network as your HDHomeRun device
1. iPhone has internet connection

## Setup
1. Download the [HDHomerun - DVR Tookit](https://github.com/carlknutson/ios-shortcuts/releases) iOS shortcut.
1. If you have just one HDHomeRun device on your network, you are ready to mass delete away!
1. If you have you more than one HDHomeRun device on your network, choose which device you would like to control. Then copy the `device ID` printed on the bottom of the unit. Replace the first `Text` field value (`hdhomerun.local`) with the device ID (e.g. `http://104fffff.local`).