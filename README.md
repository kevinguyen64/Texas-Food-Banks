# Texas Food Banks
#### Video Demo: https://youtu.be/CM_Htm6qVDA
#### Description:

"Texas Food Banks" is a website that serves as a repository for all the majors food banks
in the state of Texas. On the website, the users can access each individual food bank
and find out more information about them. Each food bank webpage provides a description
of the food bank along with the counties they serve, their address, their phone number,
and a link to their official website.

#### Purpose:

I created this website with the intent of making a difference for the Texas community. Food
insecurity is a major issue in the state of Texas and I hope my website can be a resource for
people to come and find their nearest food bank. Whether their purpose may be to obtain food
or are looking for ways to volunteer to distribute food, my website provides the necessary means
to get in contact with the food bank that covers their area.

#### Languages and Files:

- ##### Frameworks:

        Frameworks utilized: Flask, Bootstrap, W3Schools, Cloudflare

- ##### HTML (in the templates directory):

     -   **layout.html:**

                Layout.html, with the incorporation of jinja, was used as the template to all the webpages
                of the website. This file contains markup for the header of the website that includes the
                background video of the waving flag, title, background color, and navigation bar. The navigation
                bar has links to the homepage and contact page, a dropdown menu of all the food banks, and a
                search bar and search button. The links and scripts to the frameworks were contained here.

     -   **index.html:**

                Index.html contains the markup for the homepage of the website. There are 21 major food banks
                in the state of Texas and I grouped them by geographic locations. For applicable food banks, the
                image tag contains a photo of the front of their building to provide a visual of what the food bank
                looks like. The image tag is followed by a form tag that assigns a value to each food bank from
                1 to 21 (for database querying purposes). Then, there are 2 paragraph tags that provide the address
                and phone number of each food bank. Finally, there is a button tag that takes the user back to the
                top of the webpage.

     -   **bank.html:**

                Bank.html contains the markup for each individual food bank. Using jinja and SQLite, information such
                as a food bank's name, image, description, address, phone number, official website, and counties covered
                are provided for. The counties are presented in a list format for a better read for the users.

     -   **failure.html:**

                Failure.html contains the markup in the case the user provides an invalid search. They will be prompted
                a page that shows what they inputted in the search box along with a redirect back to the homepage.

     -   **contact.html:**

                Contact.html contains the markup for the contact webpage where the users can send me a message. I provided
                a purpose statement for the website along with encouragement for feedback. The users can send me a message
                by typing in the textarea and clicking the "Send!" button. The users will then be flashed with a message
                indicating a successful send.

- ##### JPGs, MP4, CSS, and Javascript (all in static directory):

     -   **JPGs:**

                For the 21 major food banks, there are 21 pictures corresponding with each food bank in the static directory.
                The images of the food banks mostly comprises of the front of their building. For some, it is a different
                photo because such a picture could not be found. I insisted on using images of the front of the food banks
                to give users a visual of what the building looks like if they were to ever go there.

     -   **MP4:**

                The only video the website utilized was an mp4 file of the waving texas flag seen in the header.

     -   **CSS:**

                The styles.css file contains all of the visual formatting for the website and each of its webpage. From
                the homepage to the navigation bar to making the website responsive on all devices, CSS was used to design
                the visual presentation to the users.

     -   **Javascript:**

                The food_banks.js file contains all of the javascript implementation on the website. An array was created
                with all the names of the food banks. Using that array in the autocomplete function, with each of the user's
                keystrokes, the array is iterated to find a potential match to the user's desired food bank search. Then there
                was implementation for if the users were to click the "Enter" key to search for the food bank, negating the need
                to click the search button directly. Finally, there was implementation for a "Back to Top" button which allowed
                the users to automatically return to the top of the homepage when clicked.

- ##### TXTs, CSVs, and Databases:

     -   **requirements.txt:**

                This file contains all of the pip-installable libraries or modules needed for this program.

     -   **food_banks.txt:**

                This file contains all 21 food banks, separated by their geographical location. Along with their names,
                the city they reside in are provided.

     -   **message.csv:**

                This file was created to retain all messages sent by users from the contact page.

     -   **food_bank.db:**

                Using SQLite, this is the database that contains the two tables utilized by the website. The first 
                table contains information such as the id, name, image, description, address, phone number, and 
                official website of each food bank. The second table contains some of the counties that each food 
                bank covers. This table contains the names of the counties, along with a county id for each county. 
                There is also a column for the food bank id that corresponds with the id of a food bank from the 
                first table. This is how both tables are connected.

- ##### Python:

     -   **app.py:**

                    Initially, a Flask and SQL object are created and the templates and sessions are configured.

     -   **@app.route("/"):**

                    This route renders the index.html template, yielding the homepage of the website.

     -   **@app.route("/bank"):**

                    This route accepted both GET and POST requests.

                    The food_bank.db was called and both tables were queried using the id assigned to each food bank.
                    The first table provided the name, image, description, address, phone number, and official website
                    of the food bank in question. The second table provided the counties that food bank covered.

                    The bank.html template was rendered, yielding the webpage of the user's requested
                    food bank.

     -   **app.route("/search"):**

                    The food_bank.db was called and both tables were queried using the name assigned to each food bank.
                    All of the same information was returned as with the /bank route; the only difference was the parameter
                    used.

                    If the user typed in nothing or inputted an invalid food bank into the search box, then the user
                    was redirected to the failure.html webpage. Otherwise, if the search was successful, the user would
                    be redirected to the bank.html webpage of that specific food bank.

     -   **app.route("/contact"):**

                    This route accepted both GET and POST requests.

                    If the user had reached the webpage through a GET request, then they'll just be directed to the contact webpage.

                    If the user had submitted a message from the contact webpage through a POST request, then their messsage
                    would have been appended to the message.csv file. There are two "\n" to make sure every unique message was
                    separated by a line of whitespace. If the message sent succesfully, then the user will be flashed a message
                    indicating as such on the contact webpage.

