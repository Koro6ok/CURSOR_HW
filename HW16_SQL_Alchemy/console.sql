SELECT * from articles
LEFT JOIN article_categories ac on articles.id = ac.article_id
LEFT JOIN category c on ac.category_id = c.id