-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 25, 2017 at 09:50 PM
-- Server version: 10.1.25-MariaDB
-- PHP Version: 7.1.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `musicly`
--

-- --------------------------------------------------------

--
-- Table structure for table `album`
--

CREATE TABLE `album` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `release_date` date NOT NULL,
  `band` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `album`
--

INSERT INTO `album` (`id`, `title`, `release_date`, `band`) VALUES
(1, 'Kammel Kalamak', '2005-05-01', 1),
(2, 'Konvicted', '2006-05-01', 2),
(3, '3aks elnas', '2017-09-17', 3),
(6, 'Singles', '0000-00-00', 1),
(7, '21', '2011-02-22', 6),
(8, 'singles', '0000-00-00', 5),
(9, 'Now That\'s What I Call the Modern Songbook', '2011-02-08', 8);

-- --------------------------------------------------------

--
-- Table structure for table `artist`
--

CREATE TABLE `artist` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `dateOfBirth` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `artist`
--

INSERT INTO `artist` (`id`, `name`, `dateOfBirth`) VALUES
(1, 'Amr Diab', '1968-04-03'),
(2, 'Akon', '1985-07-09'),
(3, 'Tamer Hosny', '1900-11-10');

-- --------------------------------------------------------

--
-- Table structure for table `artist_band`
--

CREATE TABLE `artist_band` (
  `artistId` int(11) NOT NULL,
  `bandId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `artist_band`
--

INSERT INTO `artist_band` (`artistId`, `bandId`) VALUES
(1, 1),
(2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `band`
--

CREATE TABLE `band` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `band`
--

INSERT INTO `band` (`id`, `name`) VALUES
(1, 'Amr Diab'),
(2, 'Akon'),
(3, 'Cairokee'),
(4, 'ColdPlay'),
(5, 'Eminem'),
(6, 'Adele'),
(7, 'Sia'),
(8, 'OneRepublic');

-- --------------------------------------------------------

--
-- Table structure for table `featuring`
--

CREATE TABLE `featuring` (
  `bandId` int(11) NOT NULL,
  `songId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `featuring`
--

INSERT INTO `featuring` (`bandId`, `songId`) VALUES
(2, 1),
(7, 9);

-- --------------------------------------------------------

--
-- Table structure for table `genre`
--

CREATE TABLE `genre` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `genre`
--

INSERT INTO `genre` (`id`, `name`) VALUES
(1, 'Pop'),
(2, 'Jazz'),
(3, 'Classic'),
(4, 'Hip Hop'),
(5, 'Hip-Hop'),
(6, 'Rap');

-- --------------------------------------------------------

--
-- Table structure for table `genre_song`
--

CREATE TABLE `genre_song` (
  `songId` int(11) NOT NULL,
  `genreId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `genre_song`
--

INSERT INTO `genre_song` (`songId`, `genreId`) VALUES
(1, 1),
(2, 1),
(8, 1),
(9, 5),
(9, 6);

-- --------------------------------------------------------

--
-- Table structure for table `playlist`
--

CREATE TABLE `playlist` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `playlist`
--

INSERT INTO `playlist` (`id`, `name`, `description`) VALUES
(1, 'Arabic', 'Aghany 3araby om el agnaby'),
(2, 'Mix', 'Mshakel aghany'),
(6, 'Yaraaaab', 'han5allas in sha2 Allah'),
(8, 'Solution', 'found a solution online');

-- --------------------------------------------------------

--
-- Table structure for table `playlist_song`
--

CREATE TABLE `playlist_song` (
  `playlistId` int(11) NOT NULL,
  `songId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `playlist_song`
--

INSERT INTO `playlist_song` (`playlistId`, `songId`) VALUES
(1, 1),
(2, 1),
(2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `song`
--

CREATE TABLE `song` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `lyrics` text NOT NULL,
  `length` int(11) NOT NULL,
  `album` int(11) NOT NULL,
  `path` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `song`
--

INSERT INTO `song` (`id`, `name`, `lyrics`, `length`, `album`, `path`) VALUES
(1, 'Kammel Kalamak', 'Kammel Kalamak el leila dy m3ak ana', 265, 1, '/media/alaa/New Volume/Mp3/Arabic/Amr Diab/01 Kammel Kalamak.mp3'),
(2, 'Mama Africa', 'So much so much love\r\nso much\r\nso tell me can you feel it', 265, 2, '/media/alaa/New Volume/Mp3/English/07 Akon - Mama Africa.mp3'),
(8, 'Rolling in the Deep', 'There\'s a fire starting in my heart\r\nReaching a fever pitch and it\'s bringin\' me out the dark\r\n\r\nFinally, I can see you crystal clear\r\nGo ahead and sell me out and I\'ll lay your shit bare\r\n\r\nSee how I\'ll leave with every piece of you\r\nDon\'t underestimate the things that I will do\r\n\r\nThere\'s a fire starting in my heart\r\nReaching a fever pitch and it\'s bringin\' me out the dark\r\n\r\nThe scars of your love remind me of us\r\nThey keep me thinkin\' that we almost had it all\r\n\r\nThe scars of your love, they leave me breathless\r\nI can\'t help feeling\r\n\r\nWe could have had it all\r\n(You\'re gonna wish you never had met me)\r\nRolling in the deep\r\n(Tears are gonna fall, rolling in the deep)\r\n\r\nYou had my heart inside of your hand\r\n(You\'re gonna wish you never had met me)\r\nAnd you played it to the beat\r\n(Tears are gonna fall, rolling in the deep)\r\n\r\nBaby, I have no story to be told\r\nBut I\'ve heard one on you and I\'m gonna make your head burn\r\n\r\nThink of me in the depths of your despair\r\nMake a home down there as mine sure won\'t be shared\r\n\r\n(You\'re gonna wish you never had met me)\r\nThe scars of your love remind me of us\r\n(Tears are gonna fall, rolling in the deep)\r\nThey keep me thinking that we almost had it all\r\n\r\n(You\'re gonna wish you never had met me)\r\nThe scars of your love, they leave me breathless\r\n(Tears are gonna fall, rolling in the deep)\r\nI can\'t help feeling\r\n\r\nWe could have had it all\r\n(You\'re gonna wish you never had met me)\r\nRolling in the deep\r\n(Tears are gonna fall, rolling in the deep)\r\n\r\nYou had my heart inside of your hand\r\n(You\'re gonna wish you never had met me)\r\nAnd you played it to the beat\r\n(Tears are gonna fall, rolling in the deep)\r\n\r\nCould have had it all\r\nRolling in the deep\r\n\r\nYou had my heart inside of your hand\r\nBut you played it with a beating\r\n\r\nThrow your soul through every open door (Wohh ho ho oh)\r\nCount your blessings to find what you look for (Wohh oh oh oh)\r\n\r\nTurn my sorrow into treasured gold (Wohh ho ho oh)\r\nYou\'ll pay me back in kind and reap just what you sow\r\n\r\n(You\'re gonna wish you never had met me)\r\nWe could have had it all\r\n(Tears are gonna fall, rolling in the deep)\r\n\r\nWe could have had it all\r\n(You\'re gonna wish you never had met me)\r\nIt all, it all, it all\r\n(Tears are gonna fall, rolling in the deep)\r\n\r\nWe could have had it all\r\n(You\'re gonna wish you never had met me)\r\nRolling in the deep\r\n(Tears are gonna fall, rolling in the deep)\r\n\r\nYou had my heart inside of your hand\r\n(You\'re gonna wish you never had met me)\r\nAnd you played it to the beat\r\n(Tears are gonna fall, rolling in the deep)\r\n\r\nCould have had it all\r\n(You\'re gonna wish you never had met me)\r\nRolling in the deep\r\n(Tears are gonna fall, rolling in the deep)\r\n\r\nYou had my heart inside of your hand\r\n(You\'re gonna wish you never had met me)\r\nBut you played it, you played it, you played it\r\nYou played it to the beat', 229, 7, '/home/alaa/Documents/MP3/01 Rolling in the Deep.mp3'),
(9, 'Guts Over Fear', 'Eminem</b>\r\nFeels like a close, it\'s coming to\r\nFuck am I gonna do?\r\nIt\'s too late to start over\r\nThis is the only thing I, thing I know\r\n\r\nSometimes I feel like all I ever do is\r\nFind different ways to word the same old song\r\nEver since I came along\r\nFrom the day the song called \'Hi! My Name Is\' dropped\r\nStarted thinkin\' my name was Fault\r\n\'Cause anytime things went wrong\r\nI was the one who they would blame it on\r\n\r\nThe media made me the equivalent of a modern-day Genghis Khan\r\nTried to argue it was only entertainment, dog\r\nGangsta? Nah, courageous balls\r\nHad to change my style, they said I\'m way too soft\r\nAnd I sound like AZ and Nas, out came the claws\r\nAnd the fangs been out since then\r\nBut up until the instant that I went against it\r\n\r\nIt was ingrained in me\r\nThat I wouldn\'t amount to a shit stain I thought\r\nNo wonder I had to unlearn everything my brain was taught\r\nDo I really belong in this game? I pondered\r\nI just wanna play my part\r\nShould I make waves or not?\r\nSo back and forth in my brain the tug of war wages on\r\n\r\nAnd I don\'t wanna seem ungrateful\r\nOr disrespect the art form I was raised upon\r\nBut sometimes you gotta take a loss and have people rub it in your face\r\nBefore you get made pissed off\r\nAnd keep pluggin\', it\'s your only outlet, and your only outfit\r\nSo you know they gonna talk about it\r\nBetter find a way to counter it, quick and make it, ah\r\n\r\nFeel like I\'ve already said this a kabillion eighty times\r\nHow many times can I say the same thing different ways that rhyme?\r\nWhat I really wanna say is, if there\'s anyone else that can relate to my story?\r\nBet you feel the same way I felt when I was in the same place you are\r\nWhen I was afraid to...\r\n\r\n<b>Sia</b>\r\nI was a-afraid to make a single sound\r\nAfraid I would never find a way ou-ou-out\r\nAfraid I\'d never be found\r\nI don\'t wanna go another round\r\n\r\nAn angry man\'s power will shut you up\r\nTripwires fill this house with tiptoed love\r\nRun out of excuses for everyone\r\nSo here I am and I will not run\r\n\r\nGuts over fear  (The time is near)\r\nGuts over fear (I shed a tear)\r\nFor all the times I let you push me around, I let you keep me down\r\n(But now I got) Guts over fear, guts over fear\r\n\r\n<b>Eminem</b>\r\nFeels like a close, it\'s coming to\r\nFuck am I gonna do?\r\nIt\'s too late to start over\r\nThis is the only thing I, thing I know\r\n\r\nI know what it\'s like I was there once\r\nSingle parents, hate your appearance\r\nDid you struggle to find your place in this world?\r\nAnd the pain spawns all the anger on\r\nBut it wasn\'t until I put the pain in song\r\nLearned who to aim it on that I made a spark\r\nStarted to spit hard as shit\r\nLearned how to harness it while the reins were off\r\n\r\nAnd there was a lot of bizarre shit, but the crazy part\r\nWas soon as I stopped saying \'I gave a fuck\'\r\nHaters started to appreciate my art\r\nAnd it just breaks my heart to look at all the pain I caused\r\nBut what am I gonna do when the rage is gone\r\nAnd the lights go out in that trailer park?\r\n\r\nAnd the window is closin\' and there\'s nowhere else that I can go\r\nWith flows and I\'m frozen\r\n\'Cause there\'s no more emotion for me to pull from\r\nJust a bunch of playful songs that I made for fun\r\nSo to the break of dawn here I go recycling the same old song\r\nBut I\'d rather make \'Not Afraid 2\'\r\nThan make another motherfuckin\' \'We Made You\', uh\r\n\r\nAnd I don\'t wanna seem indulgent\r\nWhen I discuss my lows and my highs\r\nMy demise and my uprise, pray to God\r\nI just open enough eyes later on\r\nGave you the supplies and the tools\r\nTo hopefully use that\'ll make you strong\r\nEnough to lift yourself up, when you feel like I felt\r\n\'Cause I can\'t explain to y\'all\r\n\r\nHow dang exhausted my legs felt\r\nJust having to balance my dang self\r\nWhen on eggshells I was made to walk\r\nBut thank you Ma, \'cause that gave me the\r\nStrength to \'cause Shady-mania\r\nSo when they empty that stadium\r\n\'Least I made it out of that house\r\nAnd found a place in this world when the day was done\r\n\r\nSo this is for every kid who all\'s they ever did\r\nWas dreamt of one day just gettin\' accepted\r\nI represent him or her, anyone similar\r\nYou are the reason that I made this song\r\nAnd everything you\'re scared to say\r\nDon\'t be afraid to say no more\r\nFrom this day forward just let them a-holes talk\r\nTake it with a grain of salt\r\nAnd eat their fuckin\' faces off\r\n\r\nThe legend of the angry blonde lives on\r\nThrough you when I\'m gone\r\nAnd to think I was a\r\n\r\n<b>Sia</b>\r\nI was a-afraid to make a single sound\r\nAfraid I would never find a way ou-ou-out\r\nAfraid I\'d never be found\r\nI don\'t wanna go another round\r\n\r\nAn angry man\'s power will shut you up\r\nTripwires fill this house with tiptoed love\r\nRun out of excuses for everyone\r\nSo here I am and I will not run\r\n\r\nGuts over fear  (The time is near)\r\nGuts over fear (I shed a tear)\r\nFor all the times I let you push me around, I let you keep me down\r\n(But now I got) Guts over fear, guts over fear', 301, 8, '/home/alaa/Documents/MP3/01 Guts Over Fear.mp3'),
(10, 'Apologize', '', 200, 9, '/home/alaa/Documents/MP3/Apologize - OneRepublic.mp3');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `album`
--
ALTER TABLE `album`
  ADD PRIMARY KEY (`id`),
  ADD KEY `band` (`band`);

--
-- Indexes for table `artist`
--
ALTER TABLE `artist`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `artist_band`
--
ALTER TABLE `artist_band`
  ADD PRIMARY KEY (`artistId`,`bandId`),
  ADD KEY `artistId` (`artistId`),
  ADD KEY `bandId` (`bandId`);

--
-- Indexes for table `band`
--
ALTER TABLE `band`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `featuring`
--
ALTER TABLE `featuring`
  ADD PRIMARY KEY (`bandId`,`songId`),
  ADD KEY `bandId` (`bandId`),
  ADD KEY `songId` (`songId`);

--
-- Indexes for table `genre`
--
ALTER TABLE `genre`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `genre_song`
--
ALTER TABLE `genre_song`
  ADD PRIMARY KEY (`songId`,`genreId`),
  ADD KEY `songId` (`songId`),
  ADD KEY `genreId` (`genreId`);

--
-- Indexes for table `playlist`
--
ALTER TABLE `playlist`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `playlist_song`
--
ALTER TABLE `playlist_song`
  ADD PRIMARY KEY (`playlistId`,`songId`),
  ADD KEY `playlistId` (`playlistId`),
  ADD KEY `songId` (`songId`);

--
-- Indexes for table `song`
--
ALTER TABLE `song`
  ADD PRIMARY KEY (`id`),
  ADD KEY `album` (`album`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `album`
--
ALTER TABLE `album`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `artist`
--
ALTER TABLE `artist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `band`
--
ALTER TABLE `band`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `genre`
--
ALTER TABLE `genre`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `playlist`
--
ALTER TABLE `playlist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `song`
--
ALTER TABLE `song`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `album`
--
ALTER TABLE `album`
  ADD CONSTRAINT `band_fk` FOREIGN KEY (`band`) REFERENCES `band` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `artist_band`
--
ALTER TABLE `artist_band`
  ADD CONSTRAINT `artist_band_fk` FOREIGN KEY (`bandId`) REFERENCES `band` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `artist_fk` FOREIGN KEY (`artistId`) REFERENCES `artist` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `featuring`
--
ALTER TABLE `featuring`
  ADD CONSTRAINT `ft_band_fk` FOREIGN KEY (`bandId`) REFERENCES `band` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `ft_song_fk` FOREIGN KEY (`songId`) REFERENCES `song` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `genre_song`
--
ALTER TABLE `genre_song`
  ADD CONSTRAINT `genre_fk` FOREIGN KEY (`genreId`) REFERENCES `genre` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `song_fk` FOREIGN KEY (`songId`) REFERENCES `song` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `playlist_song`
--
ALTER TABLE `playlist_song`
  ADD CONSTRAINT `playlist_fk` FOREIGN KEY (`playlistId`) REFERENCES `playlist` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `playlist_song_fk` FOREIGN KEY (`songId`) REFERENCES `song` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `song`
--
ALTER TABLE `song`
  ADD CONSTRAINT `album_fk` FOREIGN KEY (`album`) REFERENCES `album` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
