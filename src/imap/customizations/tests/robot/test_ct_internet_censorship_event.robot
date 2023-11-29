# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s imap.customizations -t test_internet_censorship_event.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src imap.customizations.testing.IMAP_CUSTOMIZATIONS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/imap/customizations/tests/robot/test_internet_censorship_event.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Internet censorship event
  Given a logged-in site administrator
    and an add Internet censorship event form
   When I type 'My Internet censorship event' into the title field
    and I submit the form
   Then a Internet censorship event with the title 'My Internet censorship event' has been created

Scenario: As a site administrator I can view a Internet censorship event
  Given a logged-in site administrator
    and a Internet censorship event 'My Internet censorship event'
   When I go to the Internet censorship event view
   Then I can see the Internet censorship event title 'My Internet censorship event'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Internet censorship event form
  Go To  ${PLONE_URL}/++add++Internet censorship event

a Internet censorship event 'My Internet censorship event'
  Create content  type=Internet censorship event  id=my-internet_censorship_event  title=My Internet censorship event

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Internet censorship event view
  Go To  ${PLONE_URL}/my-internet_censorship_event
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Internet censorship event with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Internet censorship event title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
