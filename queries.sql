-- QUERIES SQL - Parte 4 do Exercício

-- 1. Todos os posts, ordenados pela data, sendo o mais recente primeiro
SELECT * FROM posts_post
ORDER BY data_postagem DESC;


-- 2. Para um post com comentários, todos os seus comentários
-- (substitua o 1 pelo ID de um post que tenha comentários)
SELECT * FROM posts_comment
WHERE post_id = 1;


-- 3. Para um post com comentários, todos os seus comentários, incluindo todas as colunas 
-- da tabela comentários (exceto o post_id), o título do post e sua data de publicação, 
-- renomeada para post_date
-- (substitua o 1 pelo ID de um post que tenha comentários)
SELECT 
    c.id,
    c.texto,
    c.data_postagem,
    c.autor_id,
    p.titulo,
    p.data_postagem AS post_date
FROM posts_comment c
INNER JOIN posts_post p ON c.post_id = p.id
WHERE c.post_id = 1;


-- 4. Para uma categoria, todos os posts pertencentes a ela, incluindo as colunas 
-- da tabela de categoria e da tabela de posts
-- (substitua o 1 pelo ID de uma categoria)
SELECT 
    cat.id AS category_id,
    cat.nome AS category_nome,
    cat.descricao AS category_descricao,
    p.*
FROM posts_category cat
INNER JOIN posts_post_categorias pc ON cat.id = pc.category_id
INNER JOIN posts_post p ON pc.post_id = p.id
WHERE cat.id = 1;


-- 5. Todas as categorias que possuem dois ou mais posts
SELECT 
    cat.id,
    cat.nome,
    cat.descricao,
    COUNT(pc.post_id) AS num_posts
FROM posts_category cat
INNER JOIN posts_post_categorias pc ON cat.id = pc.category_id
GROUP BY cat.id, cat.nome, cat.descricao
HAVING COUNT(pc.post_id) >= 2;
