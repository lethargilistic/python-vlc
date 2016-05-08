import unittest
import time

try:
    import vlc
except ImportError:
    import generated.vlc as vlc

class TestMedia(unittest.TestCase):
    def setUp(self):
        self.real_m = vlc.Media("file://assets/ChopinOp9No2.mp3")

        self.mock_m = vlc.Media("file://assets/ChopinOp9No2.mp3")
        self.mock_m.set_meta(vlc.Meta.Title, 'Title')
        self.mock_m.set_meta(vlc.Meta.Artist, 'Artist')
        self.mock_m.set_meta(vlc.Meta.Genre, 'Genre')
        self.mock_m.set_meta(vlc.Meta.Copyright, 'Copyright')
        self.mock_m.set_meta(vlc.Meta.Album, 'Album')
        self.mock_m.set_meta(vlc.Meta.TrackNumber, 'TrackNumber')
        self.mock_m.set_meta(vlc.Meta.Description, 'Description')
        self.mock_m.set_meta(vlc.Meta.Rating, 'Rating')
        self.mock_m.set_meta(vlc.Meta.Date, 'Date')
        self.mock_m.set_meta(vlc.Meta.Setting, 'Setting')
        self.mock_m.set_meta(vlc.Meta.URL, 'URL')
        self.mock_m.set_meta(vlc.Meta.Language, 'Language')
        self.mock_m.set_meta(vlc.Meta.NowPlaying, 'NowPlaying')
        self.mock_m.set_meta(vlc.Meta.Publisher, 'Publisher')
        self.mock_m.set_meta(vlc.Meta.EncodedBy, 'EncodedBy')
        self.mock_m.set_meta(vlc.Meta.ArtworkURL, 'ArtworkURL')
        self.mock_m.set_meta(vlc.Meta.TrackID, 'TrackID')
        self.mock_m.set_meta(vlc.Meta.TrackTotal, 'TrackTotal')
        self.mock_m.set_meta(vlc.Meta.Director, 'Director')
        self.mock_m.set_meta(vlc.Meta.Season, 'Season')
        self.mock_m.set_meta(vlc.Meta.Episode, 'Episode')
        self.mock_m.set_meta(vlc.Meta.ShowName, 'ShowName')
        self.mock_m.set_meta(vlc.Meta.Actors, 'Actors')
        #self.mock_m.set_meta(vlc.Meta.AlbumArtist, 'AlbumArtist')
        #self.mock_m.set_meta(vlc.Meta.DiscNumber, 'DiscNumber')
        #self.mock_m.set_meta(vlc.Meta.DiscTotal, 'DiscTotal')

    def test_get_meta_title(self):
        self.assertEqual(self.mock_m.get_meta(vlc.Meta.Title), 'Title')

    def test_get_meta_artist(self):
        self.assertEqual(self.mock_m.get_meta(vlc.Meta.Artist), 'Artist')

    def test_get_meta_genre(self):
        self.assertEqual(self.mock_m.get_meta(vlc.Meta.Genre), 'Genre')

    def test_get_meta_copyright(self):
        self.assertEqual(self.mock_m.get_meta(vlc.Meta.Copyright), 'Copyright')

    def test_get_meta_album(self):
        self.assertEqual(self.mock_m.get_meta(vlc.Meta.Album), 'Album')

    def test_get_meta_tracknumber(self):
        self.assertEqual(self.mock_m.get_meta(vlc.Meta.TrackNumber), 'TrackNumber')

    def test_get_meta_description(self):
        self.assertEqual(self.mock_m.get_meta(vlc.Meta.Description), 'Description')

    def test_get_meta_rating(self):
        self.assertEqual(self.mock_m.get_meta(vlc.Meta.Rating), 'Rating')

    def test_get_meta_date(self):
        self.assertEqual(self.mock_m.get_meta(vlc.Meta.Date), 'Date')

    def test_get_meta_setting(self):
        self.assertEqual(self.mock_m.get_meta(vlc.Meta.Setting), 'Setting')

    def test_get_meta_url(self):
        self.assertEqual(self.mock_m.get_meta(vlc.Meta.URL), 'URL')

    def test_get_meta_language(self):
        self.assertEqual(self.mock_m.get_meta(vlc.Meta.Language), 'Language')

    def test_get_meta_nowplaying(self):
        self.assertEqual(self.mock_m.get_meta(vlc.Meta.NowPlaying), 'NowPlaying')

    def test_get_meta_publisher(self):
        self.assertEqual(self.mock_m.get_meta(vlc.Meta.Publisher), 'Publisher')

    def test_get_meta_encodedby(self):
        self.assertEqual(self.mock_m.get_meta(vlc.Meta.EncodedBy), 'EncodedBy')

    def test_get_meta_artworkurl(self):
        self.assertEqual(self.mock_m.get_meta(vlc.Meta.ArtworkURL), 'ArtworkURL')

    def test_get_meta_trackid(self):
        self.assertEqual(self.mock_m.get_meta(vlc.Meta.TrackID), 'TrackID')

    def test_get_meta_tracktotal(self):
        self.assertEqual(self.mock_m.get_meta(vlc.Meta.TrackTotal), 'TrackTotal')

    def test_get_meta_director(self):
        self.assertEqual(self.mock_m.get_meta(vlc.Meta.Director), 'Director')

    def test_get_meta_season(self):
        self.assertEqual(self.mock_m.get_meta(vlc.Meta.Season), 'Season')

    def test_get_meta_episode(self):
        self.assertEqual(self.mock_m.get_meta(vlc.Meta.Episode), 'Episode')

    def test_get_meta_showname(self):
        self.assertEqual(self.mock_m.get_meta(vlc.Meta.ShowName), 'ShowName')

    def test_get_meta_actors(self):
        self.assertEqual(self.mock_m.get_meta(vlc.Meta.Actors), 'Actors')

    #def test_get_meta_albumartist(self):
    #    self.assertEqual(self.mock_m.get_meta(vlc.Meta.AlbumArtist), 'AlbumArtist')

    #def test_get_meta_discnumber(self):
    #    self.assertEqual(self.mock_m.get_meta(vlc.Meta.DiscNumber), 'DiscNumber')

    #def test_get_meta_disctotal(self):
    #    self.assertEqual(self.mock_m.get_meta(vlc.Meta.DiscTotal), 'DiscTotal')

    def test_get_mrl(self):
        self.assertEqual(self.real_m.get_mrl(), "file://assets/ChopinOp9No2.mp3")

    def test_get_state_nothing_special(self):
        self.assertEqual(self.real_m.get_state(), vlc.State.NothingSpecial)

    def test_get_state_opening(self):
        player = vlc.MediaPlayer()
        player.set_media(self.real_m)
        player.play()
        self.assertEquals(self.real_m.get_state(), vlc.State.Opening)

    def test_get_state_playing(self):
        player = vlc.MediaPlayer()
        player.set_media(self.real_m)
        player.play()
        while self.real_m.get_state() == vlc.State.Opening:
            pass
        self.assertEquals(self.real_m.get_state(), vlc.State.Playing)

    def test_get_state_paused(self):
        player = vlc.MediaPlayer()
        player.set_media(self.real_m)
        player.play()
        while self.real_m.get_state() == vlc.State.Opening:
            pass
        player.pause()
        self.assertEquals(self.real_m.get_state(), vlc.State.Paused)

    def test_get_state_paused_then_resumed(self):
        player = vlc.MediaPlayer()
        player.set_media(self.real_m)
        player.play()
        while self.real_m.get_state() == vlc.State.Opening:
            pass
        player.pause()
        player.pause()
        self.assertEquals(self.real_m.get_state(), vlc.State.Playing)

    def test_get_state_stopped(self):
        player = vlc.MediaPlayer()
        player.set_media(self.real_m)
        player.play()
        while self.real_m.get_state() == vlc.State.Opening:
            pass
        player.stop()
        self.assertEquals(self.real_m.get_state(), vlc.State.Stopped)

    #TODO, not sure how to advance it to the end.
    #def test_get_state_ended(self):
    #    player = vlc.MediaPlayer()
    #    player.set_media(self.real_m)
    #    player.play()
    #    
    #    self.assertEquals(self.real_m.get_state(), vlc.State.Stopped)

    def test_is_parsed_false(self):
        self.assertFalse(self.real_m.is_parsed())

    def test_is_parsed_true(self):
        self.real_m.parse()
        self.assertTrue(self.real_m.is_parsed())

    def test_duplicate(self):
        dup = self.real_m.duplicate()
        self.assertEqual(self.real_m.get_mrl(), dup.get_mrl())

    def test_player_new_from_media(self):
        otherplayer = vlc.MediaPlayer("file://assets/ChopinOp9No2.mp3")
        self.assertEqual(self.real_m.player_new_from_media().get_media().get_mrl(), 
                         otherplayer.get_media().get_mrl())

