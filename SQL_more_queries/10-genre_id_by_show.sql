-- Import the database dump from hbtn_0d_tvshows to your MySQL server

-- > curl -o hbtn_0d_tvshows.sql https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- > mysql -hlocalhost -uroot -p -e "CREATE DATABASE IF NOT EXISTS hbtn_0d_tvshows;"
-- > mysql -hlocalhost -uroot -p hbtn_0d_tvshows < hbtn_0d_tvshows.sql

-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows, tv_show_genres WHERE genre_id > 0 ORDER BY tv_shows.title;