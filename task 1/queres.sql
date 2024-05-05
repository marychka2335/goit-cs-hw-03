--drop table tasks, users , status 
--Отримати всі завдання певного користувача. Використайте SELECT для отримання завдань конкретного користувача за його user_id.
SELECT * 
FROM tasks t 
WHERE user_id = 9;
--Вибрати завдання за певним статусом. Використайте підзапит для вибору завдань з конкретним статусом, наприклад, 'new'.
SELECT * FROM tasks t
JOIN status s ON t.status_id = s.id
WHERE s.name = 'new';
--Оновити статус конкретного завдання. Змініть статус конкретного завдання на 'in progress' або інший статус.
UPDATE status 
SET name = 'new'
WHERE id = 2;
--Отримати список користувачів, які не мають жодного завдання. Використайте комбінацію SELECT, WHERE NOT IN і підзапит.
SELECT * FROM users
WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);
--Додати нове завдання для конкретного користувача. Використайте INSERT для додавання нового завдання.
INSERT INTO  status (name) 
VALUES('new');
INSERT INTO  tasks(title, description, user_id, status_id) 
VALUES('write essay', 'write essay about nature, text must be from 300 till 500 words', 1 , 1001);
--Отримати всі завдання, які ще не завершено. Виберіть завдання, чий статус не є 'завершено'.
SELECT * FROM tasks t
JOIN status s ON t.status_id = s.id
WHERE s.name != 'in progress';
--Видалити конкретне завдання. Використайте DELETE для видалення завдання за його id.
DELETE FROM tasks WHERE id = 1001;
--Знайти користувачів з певною електронною поштою. Використайте SELECT із умовою LIKE для фільтрації за електронною поштою.
SELECT * FROM users WHERE email LIKE '%@example.com';
--Оновити ім'я користувача. Змініть ім'я користувача за допомогою UPDATE.
UPDATE users SET fullname = 'Peter Pen' WHERE id = 1;
--Отримати кількість завдань для кожного статусу. Використайте SELECT, COUNT, GROUP BY для групування завдань за статусами.
SELECT status.name, COUNT(tasks.id) AS task_count
FROM status
LEFT JOIN tasks ON status.id = tasks.status_id
GROUP BY status.name;
--Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти. Використайте SELECT з умовою LIKE в поєднанні з JOIN, щоб вибрати завдання, призначені користувачам, чия електронна пошта містить певний домен (наприклад, '%@example.com').
SELECT tasks.*
FROM tasks
JOIN users ON tasks.user_id = users.id
WHERE users.email LIKE '%@example.com';
--Отримати список завдань, що не мають опису. Виберіть завдання, у яких відсутній опис.
SELECT *
FROM tasks
WHERE description IS NULL OR description = '';
--Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. Використайте INNER JOIN для отримання списку користувачів та їхніх завдань із певним статусом.
SELECT u.fullname, t.title, t.description
FROM users u
INNER JOIN tasks t ON u.id = t.user_id
INNER JOIN status s ON t.status_id = s.id
WHERE s.name = 'in progress';
--Отримати користувачів та кількість їхніх завдань. Використайте LEFT JOIN та GROUP BY для вибору користувачів та підрахунку їхніх завдань.
SELECT u.fullname, COUNT(t.id) AS task_count
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.fullname;