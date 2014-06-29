from selenium import webdriver
from django import TestCase
browser = webdriver.Firefox()
# Jane Doe is a new patient at the Midvale Clinic. 
# As a first step she needs to fill out her family history/ demographic information at the front desk
# She has the option of either going to the clinic directly or calling them up on the phone.
# The front desk gives her a URL to go to.
browser.get('http://localhost:8000')
# She is also given an intial usr name and pwd to enter into her account, which she MUST change after logging in for the first time.
# Jane sees the login page prompting her to enter her clinic-made usr name and pwd.

# After Jane enters it, she is taken to a 'customize account' page, where she can set-up her own username and pwd that will be 
# easy for her to remember. 
# She hits enter.
# Jane now notices that she's in a page, with the first tab on it, titled 'demographic information'.
# She also notices on this page, it says 'welcome Jane Doe' on the top-right-hand-corner of the screen. 
# She also notices all other tabs (tab2: 'Personal Health History'; tab3: 'Family Health History' )
# in this particular page are disabled. 
# She notices that she has only two options now: Either start filling up the demographic information or exit her account
# With no choice left, she fills up the form. She notices that when she's done with the last field, the 'next' button in
# that tab gets activated. 
# So she hits the 'next' button and it takes her to the next tab which is the 'personal history' tab.
# Again she fills up her personal health history questions and quickly moves on to the next tab, buu clicking 'next' here. 
# She proceeds to fill up the 'family history' questions. 
# when she's done with it, instead of next button, she notices a 'submit' button gets activated here.
# She presses the submit button and she sees a screen that says 'Thank You Jane Doe. You are now set for your next appointment.'
# Jane Doe is need of medical attention quite often. So she visits the clinic quite often. Everytime she visits, she is given an ipad that
# displays the cilnic's login page. she verifies her demographic/ insurance informaiton and waits for a dcotor to see her.
# During the visit the doctor enter all clinically pertinent informaiton into her health record.
# Forward a few visits later...
# Jane Doe is at home, feeling better and happy. She tries to recollect the treatment options that she has had in the past, which ultimately 'cured' her of her illness.
# Think as she might, she is not able to jog her memory past two visits. She remembers the doctor mentioning that her record will be available to her at any time for her
# as a 'view only' option.
# She types in www.MyMidvaleClinicRecord.com which takes her to a log in screen that looked very similar to the one she has seen  at the clinic
# She notices that there is a list of options on the left, which must have been visible to her everytime she loggedin. She just di not pay attention until now.
# She chooses the first one that says'Problem List'. Not sure what 'problem list' is, she decides to click and see what it's about
# She sees a list of conditions that she has been expereiencing in the past since she became a patient at the Midvale Clinic.
# She notices that the heading 'problem list' iteself has an 'i' button next to it and also almost most items on the list had the 'i' button next to it.
# Curious, she hits the 'i' button next to 'problem list' and is surprisingly taken to another tab in the browser: a link to AHIMA's webpage that had the definition for problem list.
# She is now able to see/ understand her 'Problem Listand glances through the links that read:'Dianoses', 'Test Results', 'Treatment', 'Email Clinician', 'Schedule Appointment'
# She decides to investigate th other links at a later time and logs out.

browser.quit()
