## HDHomeRun DVR Tookit

#### Download [link](https://www.icloud.com/shortcuts/db6a1801e56e4c4bba40a3821a3b8247)

The HDHomeRun DVR Toolkit is an iOS shortcut designed to simplify and enhance the management of your HDHomeRun DVR. While the native HDHomeRun DVR is stable and reliable, it lacks features that make maintaining recordings easier. This toolkit bridges those gaps with:
- **Series Recording Tracking**: By leveraging the TVmaze API, the shortcut can estimate how many episodes of a season you’ve already recorded. While not perfect, it works effectively in most cases.
- **Storage Alerts**: The HDHomeRun DVR doesn’t notify you when your storage is nearing capacity. To address this, the shortcut can detect available storage space and notify if it is low. More details on this in the [setup](#alert-on-low-hard-drive-space) section below.
- **Bulk Recording Management**: Easily delete multiple recordings at once, saving time and effort.
With these features, the HDHomeRun DVR Toolkit helps you efficiently manage DVR space and recordings, ensuring you get the most out of your HDHomeRun setup.
<div width=100%>
    <img src="ScreenRecording_delete.gif" width="20%" height="20%" title="Mass delete recordings"/>
    <img src="ScreenRecording_storage_details.gif" width="20%" height="20%" title="View DVR storage details"/>
    <img src="ScreenRecording_recording_details.gif" width="20%" height="20%" title="View recording details for tv show"/>
</div>

## Getting Started

### Pre-requites
1. [a-Shell](https://apps.apple.com/us/app/a-shell/id1473805438) installed and configured on iPhone
    1. Open a-Shell, and execute the following command: `curl hdhomerun.local`
    1. You should receive a pop-up that states `"a-Shell" would like to find and connect to devices on your local network ...",` select `Allow`
    1. If you do not see the pop-up, or you mistakenly selected `Don't Allow`, you can access this toggle setting from iOS `Settings` app -> `a-Shell` -> `Local Network`
    1. If the `Local Network` toggle is enabled, but you are still having issues with connecting to `hdhomerun.local`, restart the phone and try connecting again, trust me :)
1. iPhone is connected to same network as your HDHomeRun device
1. iPhone has internet connection

### General Setup
1. Download the [HDHomerun - DVR Tookit](#download-link) iOS shortcut.
1. If you have just one HDHomeRun device on your network, you are ready to mass delete away!
1. If you have you more than one HDHomeRun device on your network, choose which device you would like to control. Then copy the `device ID` printed on the bottom of the unit. Opening the shortcut to edit, towards the top will be a dictionary that contains key and values. Replace the `url` value from `hdhomerun.local` to the device ID (e.g. `http://104fffff.local`).

### Alert on Low Hard Drive Space
1. Set Up an Automation:
    - Create an automation in the Shortcuts app to execute daily (or your preferred cadence).
    - Configure it to run without requiring confirmation.
    - Disable notifications for the automation.
1. Trigger the HDHomeRun Shortcut: 
    - Ensure the automation triggers the HDHomeRun shortcut correctly by sending input when executing the shortcut.
    - This input is necessary for the shortcut to determine disk space usage.
1. Network Considerations:
    - The shortcut requires your iPhone to be connected to the local network to function.
    - For added flexibility, you can modify the shortcut to check if you are on your home network before executing.
1. Adjust the Alert Threshold:
    - By default, the shortcut alerts at 90% disk usage.
    - To change this threshold, locate the dictionary at the top of the shortcut and modify the alert-threshold property with your desired value.
