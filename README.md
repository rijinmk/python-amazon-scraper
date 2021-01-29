# python-amazon-scraper
Keeps watching a link for prices and stock

- Tasks
    - Part #1 [29/01/2021]
        - Watching Amazon 
            - Read HTML 
            - Find 2 things:
                - The stock
                - The price
            - History delete-r
                - After 10 readings, delete 0-4
            - 
        - Methods of notifying the user
            (best to worst)
            - [A] Twilio to send SMS 
            - [B] Email
            - [C] Loud Sound
            

https://www.amazon.ae/s?k=ps5
crid=3PIS1G7OWORVO
sprefix=P%2Caps%2C311
ref=nb_sb_ss_ts-a-p_1_1

- Search term "PS5"
- Loop through each div
    - Specifically s-result-item
    - In s-result-item
        - soup.find('li', {'class': 'text'})