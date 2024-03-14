-- Keep a log of any SQL queries you execute as you solve the mystery.
--SELECT DISTINCT description FROM crime_scene_reports

--SELECT DISTINCT description FROM crime_scene_reports Where description like "%bakery%";

--interviews
--SELECT * FROM interviews where transcript like "%bakery%";


--1. suspicious
--SELECT bank_accounts.account_number, person_id, license_plate FROM atm_transactions
-- select * from people where phone_number =
-- (select receiver from phone_calls where caller = (
-- \

SELECT * FROM atm_transactions
join bank_accounts on bank_accounts.account_number = atm_transactions.account_number
join people on people.id = bank_accounts.person_id
where year = 2023
and month = 7
and day = 28
and  transaction_type = 'withdraw'
and atm_location = 'Leggett Street'
AND license_plate in
                (SELECT license_plate FROM bakery_security_logs where year = 2023 and month = 7 and day = 28 and activity = 'exit' and hour = 10 and minute < 30)
AND phone_number in
                (select phone_number from people where phone_number in (SELECT caller FROM phone_calls where year = 2023 and month = 7 and day = 28 and duration <= 60))
AND passport_number in
                ( SELECT passport_number FROM passengers WHERE flight_id = (SELECT id FROM flights where year = 2023 and month = 7 and day = 29 order by hour limit 1));



SELECT * FROM flights where year = 2023 and month = 7 and day = 29 order by hour limit 1;

SELECT * FROM airports;

                -- ) and year = 2023 and month = 7 and day = 28 and duration <= 60);


-- SELECT * FROM phone_calls where year = 2023 and month = 7 and day = 28 and duration <= 60;
-- --2.suspicious
-- SELECT * FROM bakery_security_logs where year = 2023 and month = 7 and day = 28 and activity = 'exit' and hour = 10;

--calls
-- select * from people where phone_number in(
-- SELECT caller FROM phone_calls
-- where year = 2023 and month = 7 and day = 28 and duration <= 60);


--  SELECT passport_number
-- FROM passengers
-- WHERE flight_id =
--                 (SELECT id FROM flights where year = 2023 and month = 7 and day = 29 order by hour limit 1)

-- SELECT *
-- FROM bakery_security_logs
-- where year = 2023 and
--       month = 7 and
--       day = 28 and
--       activity = 'exit' and
--       hour = 10 and
--       license_plate in (
--                         SELECT license_plate
--                         FROM people
--                         WHERE passport_number in (
--                                                   SELECT passport_number
--                                                   FROM passengers
--                                                   WHERE flight_id =
--                                                                     (SELECT id FROM flights where year = 2023 and month = 7 and day = 29 order by hour limit 1))) and license_plate in (select license_plate from people where phone_number in(
--                         SELECT caller FROM phone_calls
--                         where year = 2023 and month = 7 and day = 28 and duration <= 60)) and license_plate in (SELECT license_plate FROM atm_transactions
--                         join bank_accounts on bank_accounts.account_number = atm_transactions.account_number
--                         join people on people.id = bank_accounts.person_id
--                         where year = 2023 and month = 7 and day = 28 and  transaction_type = 'withdraw' and atm_location = 'Leggett Street')
-- ;

-- SELECT * from bank_accounts;
