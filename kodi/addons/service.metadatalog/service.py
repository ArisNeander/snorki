import xbmc
import xbmc.Player
import os

# Where to save the metadata file (change if you want another path)
OUTFILE = xbmc.translatePath("special://profile/metadata_log.txt")

class MetadataLogger(xbmc.Player):
    def __init__(self):
        super().__init__()

    def onPlayBackStarted(self):
        xbmc.sleep(1000)  # give Kodi a moment to load metadata
        self.log_metadata("Started")

    def onAVChange(self):
        # Called when metadata changes during playback
        self.log_metadata("Changed")

    def log_metadata(self, event="Update"):
        info = self.getMusicInfoTag()
        if not info:
            return

        artist = info.getArtist()
        title = info.getTitle()

        try:
            with open(OUTFILE, "w", encoding="utf-8") as f:
                f.write(f"Event: '{event}'\n")
                f.write(f"Artist: '{artist}'\n")
                f.write(f"Title: '{title}'\n")
            xbmc.log(f"[MetadataLogger] {event}: {artist} - {title}", xbmc.LOGINFO)
        except Exception as e:
            xbmc.log(f"[MetadataLogger] Error writing file: {e}", xbmc.LOGERROR)

if __name__ == "__main__":
    player = MetadataLogger()
    monitor = xbmc.Monitor()
    while not monitor.abortRequested():
        if monitor.waitForAbort(1):
            break
