import xbmc
import xbmcgui
import xbmc.Player
import re

class MetadataFixer(xbmc.Player):
    def __init__(self):
        super().__init__()
        self.regex = re.compile(r"^(.*?)\s*-\s*(.*)$")  # matches "Artist - Title"

    def onPlayBackStarted(self):
        xbmc.sleep(1000)  # wait a moment for metadata
        self.fix_metadata()

    def onPlayBackStopped(self):
        pass

    def fix_metadata(self):
        li = self.getMusicInfoTag()
        if not li:
            return
        title = li.getTitle()
        artist = li.getArtist()

        # Some radio streams put the full "Artist - Title" in Title
        if self.regex.match(title) and not artist:
            artist_part, title_part = self.regex.match(title).groups()
            li.setArtist(artist_part.strip())
            li.setTitle(title_part.strip())
            xbmc.log(f"[MetadataSwap] Fixed: {artist_part} / {title_part}", xbmc.LOGINFO)

if __name__ == "__main__":
    player = MetadataFixer()
    monitor = xbmc.Monitor()
    while not monitor.abortRequested():
        if monitor.waitForAbort(1):
            break
