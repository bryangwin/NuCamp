INSERT INTO users(username, password, profile_picture, email, phone_number)
VALUES
('user1', 'pass1', 'http://link-to-user1-profile-picture.com', 'user1@email.com', '1234567890'),
('user2', 'pass2', 'http://link-to-user2-profile-picture.com', 'user2@email.com', '0987654321');

INSERT INTO user_followers(user_id, follower_id)
VALUES
(1, 2),   -- user1 is followed by user2
(2, 1);   -- user2 is followed by user1

INSERT INTO user_following(user_id, following_id) 
VALUES 
(1, 2),   -- user1 is following user2
(2, 1);   -- user2 is following user1

INSERT INTO posts(user_id, image, caption, date) 
VALUES 
(1, 'http://link-to-post1-image.com', 'caption for post 1', NOW()),   -- user1 makes a post
(2, 'http://link-to-post2-image.com', 'caption for post 2', NOW());  -- user2 makes a post

INSERT INTO post_likes(post_id, user_id) 
VALUES 
(1, 2),   -- user2 likes post1
(2, 1);   -- user1 likes post2

INSERT INTO comments(post_id, user_id, text, date) 
VALUES 
(1, 2, 'comment from user2 on post1', NOW()),   -- user2 comments on post1
(2, 1, 'comment from user1 on post2', NOW());  -- user1 comments on post2

INSERT INTO comment_likes(comment_id, user_id) 
VALUES 
(1, 2),   -- user2 likes comment1
(2, 1);   -- user1 likes comment2

