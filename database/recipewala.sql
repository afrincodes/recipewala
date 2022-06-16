-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 04, 2022 at 10:21 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `recipewala`
--

-- --------------------------------------------------------

--
-- Table structure for table `add_recipe`
--

CREATE TABLE `add_recipe` (
  `recipe_id` int(11) NOT NULL,
  `chef_email` varchar(200) NOT NULL,
  `name` varchar(100) NOT NULL,
  `ingredient` varchar(2000) NOT NULL,
  `vntype` varchar(10) NOT NULL,
  `cuisine` varchar(50) NOT NULL,
  `description` varchar(5000) NOT NULL,
  `photo` varchar(355) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `add_recipe`
--

INSERT INTO `add_recipe` (`recipe_id`, `chef_email`, `name`, `ingredient`, `vntype`, `cuisine`, `description`, `photo`) VALUES
(31, 'kunal@gmail.com', 'Veg Fried Rice Recipe | Veg Pulaw Recipe | Indian Recipes', '1 cup basmati rice\r\n          1 tsp  oil\r\n          ½ tsp salt\r\n          water for soaking & boiling\r\n          for fried rice:\r\n          2 tbsp oil\r\n          2 clove garlic (finely chopped)\r\n          ½ onion (finely chopped)\r\n          4 tbsp spring onion (chopped)\r\n          ¼ carrot (finely c', 'veg', 'Indian', 'To prepare nonsticky rice, soak the rice for 20 mins in water. after 20 minutes, take a vessel. pour water and get to boiling. put the soaked and drained rice in the vessel. add a teaspoon of oil to it. cook until the rice is almost cooked yet separated and not mushy. drain the rice into the colander and allow it to cool. preventing them from getting dried up, you can cover and keep them aside. now you’ll get perfect nonsticky rice.', 'card1.jpg'),
(32, 'pooja@gmail.com', 'Mcdonald Style Burger Meal Combo Recipe | Burger And French Fries', '1 pound ground lean (7% fat) beef\r\n          1 large egg\r\n          ½ cup minced onion\r\n          ¼ cup fine dried bread crumbs\r\n          1 tablespoon Worcestershire\r\n          1 or 2 cloves garlic, peeled and minced\r\n          About 1/2 teaspoon salt\r\n          About 1/4 teaspoon pepper\r\n         ', 'veg', 'French', 'There is a process to follow which involves parboiling potatoes and then double frying them to achieve fluffy inside and crispy outside fries. \r\n\r\nSimply cutting potatoes and frying them results into soggy fries, because as we cut potatoes into strips the starch (Starch is simple sugars) is released which when comes in contact with hot oil caramelises quickly.  It gives a thin delicate crust that’s quickly softened by the interior’s moisture.', 'card2.jpg'),
(33, 'sanjeev@gmail.com', 'Healthy & Tasty Veg Fry Recipe | Indian Food', 'French beans 1/4 kg stringed and chop into small pieces (par boil with salt and turmeric for 7-8 mts)\r\n          Pappula podi 2 1/2 tbsps\r\n          Salt to taste\r\n          Cooking oil 1/2 tbsp\r\n          For tempering/poppu/tadka:\r\n          Mustard seeds 1/2 tsp\r\n          Dry red chillis 2 de-se', 'veg', 'Indian', 'I have a beans fry recipe for you today. I notice that there are very few recipes with beans on my blog despite me making beans often in my home. I usually make a simple indian vegetarian stir fry dish to go with a tangy dal based stew, Pappu Pulusu and rice. I used the magical Pappula Podi to jazz up some plain french beans and it took me less than 20 mts to prepare.\r\nHealthy, hearty and flavorful Andhra style beans fry that goes well with rice and sambar/pappu pulusu or with rotis.', 'card3.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `chef_signup`
--

CREATE TABLE `chef_signup` (
  `name` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `mobile` varchar(10) NOT NULL,
  `password` varchar(15) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `photo` varchar(355) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `chef_signup`
--

INSERT INTO `chef_signup` (`name`, `email`, `mobile`, `password`, `city`, `state`, `photo`) VALUES
('Afrin Saba', 'afrinsaba2002@gmail.com', '2763253174', '1234', 'Gumla', 'Jharkhand', 'product-preview-l-1.jpg'),
('Alia Siddique', 'alia@gmail.com', '3409876523', '1234', 'Gumla', 'Jharkhand', 'img4.jpg'),
('Firoz Khan', 'firoz@gmail.com', '8626518354', '1234', 'Gumla', 'Jharkhand', 'img1.jpg'),
('Kunal Kapoor', 'kunal@gmail.com', '7765545454', '1234', 'Mumbai', 'Maharastra', 'client2.jpg'),
('Mahvish Naaz', 'mahvish123@gmail.com', '5637489587', '1234', 'Gumla', 'Jharkhand', 'img4.jpg'),
('Nasrin Ara', 'nasrin@gmail.com', '8626518354', '1234', 'Gumla', 'Jharkhand', 'img2.jpg'),
('Neha Naaz', 'neha@gmail.com', '5637489587', '1234', 'Mumbai', 'Maharastra', 'img4.jpg'),
('Pooja Dhingra', 'pooja@gmail.com', '7654356478', '1234', 'Kolkata', 'West Bengal', 'client1.jpg'),
('Sanjeev Kapur', 'sanjeev@gmail.com', '3409876523', '1234', 'Jaipur', 'Rajasthan', 'img1.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `message`
--

CREATE TABLE `message` (
  `message_id` int(11) NOT NULL,
  `user_email` varchar(100) NOT NULL,
  `chef_email` varchar(100) NOT NULL,
  `recipe_id` varchar(100) NOT NULL,
  `message` varchar(255) NOT NULL,
  `reply` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `message`
--

INSERT INTO `message` (`message_id`, `user_email`, `chef_email`, `recipe_id`, `message`, `reply`) VALUES
(1, 'falak@gmail.com', 'kunal@gmail.com', '31', 'hello', 'hii'),
(2, 'falak@gmail.com', 'kunal@gmail.com', '31', 'Hello, How are you?', 'hello, I\'m Good'),
(3, 'falak@gmail.com', 'kunal@gmail.com', '31', 'Hey', 'Hey, Thanks for visiting!'),
(4, 'firoz@gmail.com', 'kunal@gmail.com', '31', 'Your recipe is awesome.', 'Thank You!'),
(5, 'firoz@gmail.com', 'kunal@gmail.com', '31', 'hi', ''),
(6, 'firoz@gmail.com', 'None', 'None', 'hello', ''),
(7, 'firoz@gmail.com', 'kunal@gmail.com', '31', 'hello', ''),
(8, 'afrinsaba2002@gmail.com', 'kunal@gmail.com', '31', 'Hello Chef,\r\nYour recipe is delicious.', 'Thank You!! :)'),
(9, 'afrinsaba2002@gmail.com', 'pooja@gmail.com', '32', 'Hello Ma\'am,\r\nHow are you?', '');

-- --------------------------------------------------------

--
-- Table structure for table `user_signup`
--

CREATE TABLE `user_signup` (
  `name` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `mobile` varchar(10) NOT NULL,
  `password` varchar(15) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `photo` varchar(355) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_signup`
--

INSERT INTO `user_signup` (`name`, `email`, `mobile`, `password`, `city`, `state`, `photo`) VALUES
('Afrin Saba', 'afrinsaba2002@gmail.com', '5637489587', '1234', 'Ranchi', 'Jharkhand', 'img4.jpg'),
('Falak Naaz', 'falak@gmail.com', '6543678877', '1234', 'Ranchi', 'Jharkhand', 'client1.jpg'),
('Firoz Khan', 'firoz@gmail.com', '7654323687', '1234', 'Ranchi', 'Jharkhand', 'img2.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `add_recipe`
--
ALTER TABLE `add_recipe`
  ADD PRIMARY KEY (`recipe_id`);

--
-- Indexes for table `chef_signup`
--
ALTER TABLE `chef_signup`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `message`
--
ALTER TABLE `message`
  ADD PRIMARY KEY (`message_id`);

--
-- Indexes for table `user_signup`
--
ALTER TABLE `user_signup`
  ADD PRIMARY KEY (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `add_recipe`
--
ALTER TABLE `add_recipe`
  MODIFY `recipe_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `message`
--
ALTER TABLE `message`
  MODIFY `message_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
