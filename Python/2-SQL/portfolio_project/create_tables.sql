CREATE TABLE users (
  ID SERIAL PRIMARY KEY,
  username VARCHAR(50) UNIQUE NOT NULL,
  password VARCHAR(50) NOT NULL,
  profile_picture VARCHAR(2000),
  email VARCHAR(50),
  phone_number VARCHAR(15)
);

CREATE TABLE user_followers (
  user_id INT NOT NULL,
  follower_id INT NOT NULL,
  PRIMARY KEY (user_id, follower_id),
  FOREIGN KEY (user_id) REFERENCES users(ID),
  FOREIGN KEY (follower_id) REFERENCES users(ID)
);

CREATE TABLE user_following (
  user_id INT NOT NULL,
  following_id INT NOT NULL,
  PRIMARY KEY (user_id, following_id),
  FOREIGN KEY (user_id) REFERENCES users(ID),
  FOREIGN KEY (following_id) REFERENCES users(ID)
);

CREATE TABLE posts (
  ID SERIAL PRIMARY KEY,
  user_id INT NOT NULL,
  image VARCHAR(2000) NOT NULL,
  caption VARCHAR,
  date TIMESTAMP NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(ID)
);

CREATE TABLE post_likes (
  post_id INT NOT NULL,
  user_id INT NOT NULL,
  PRIMARY KEY (post_id, user_id),
  FOREIGN KEY (post_id) REFERENCES posts(ID),
  FOREIGN KEY (user_id) REFERENCES users(ID)
);

CREATE TABLE comments (
  ID SERIAL PRIMARY KEY,
  post_id INT NOT NULL,
  user_id INT NOT NULL,
  text TEXT NOT NULL,
  date TIMESTAMP NOT NULL,
  FOREIGN KEY (post_id) REFERENCES posts(ID),
  FOREIGN KEY (user_id) REFERENCES users(ID)
);

CREATE TABLE comment_likes (
  comment_id INT NOT NULL,
  user_id INT NOT NULL,
  PRIMARY KEY (comment_id, user_id),
  FOREIGN KEY (comment_id) REFERENCES comments(ID),
  FOREIGN KEY (user_id) REFERENCES users(ID)
);
