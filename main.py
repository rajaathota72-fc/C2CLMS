import streamlit as st
import profile
from streamlit_option_menu import option_menu
from Database import UserData
st.set_page_config(layout='wide',page_title="Test LMS: Code to Change Jr.",page_icon="images/favicon.png",initial_sidebar_state="expanded")
st.markdown("<h2 style='text-align: center; color: #ffffff;background-color:#0ea2bd;border-radius:5px;'>C2C Jr : My Learning Portal</h2>", unsafe_allow_html=True)
#cols = st.sidebar.columns([0.2,2,1])
st.sidebar.image("Images/logo.png",use_column_width=True)
with st.sidebar:
    menu = option_menu("",
                       ['Login', "Register"],
                       icons=["person", "person-plus"], default_index=1,
                       styles={"nav-link-selected": {"background-color": "#0ea2bd"}},orientation="horizontal")
if menu == "Register":
    registration_expander = st.expander("Register Now", expanded=True)
    with registration_expander:
        cols = st.columns(2)
        name = cols[0].text_input("Full Name", placeholder="type here")
        email = cols[0].text_input("Email", placeholder="type here")
        contact = cols[1].text_input("Contact details - Whatsapp", placeholder="type here")
        password = cols[1].text_input("Set your Password", type="password")
        avatar = cols[0].selectbox("Select the avatar from list",["B1","G1","B2","G2","B3","G3"])
        cols[1].markdown("<h1></h1>",unsafe_allow_html=True)
        cols[0].image("Images/Profileavatars/avatars.png")
        cols[1].markdown("")
        cols[1].markdown("<p style='text-align:left; color: #0ea2bd;'>This is your selected avatar from the given list of avatars.</p>", unsafe_allow_html=True)
        cols[1].image("Images/Profileavatars/" + avatar + ".png", width=300)
        if cols[0].button("Click here to Register"):
            result = UserData.CreateUser(name, contact, email, password,avatar)
            if result == "success":
                st.success("Thank you for Registration and Approval pending from admin. You can access when approval is granted by admin and you will receive an email")
            else:
                st.warning("Email Already exists and try to login")
if menu == "Login":
    expander_1 = st.expander("Login Here", expanded=True)
    with expander_1:
        cols = st.columns([1, 2, 1])
        username = cols[1].text_input("Enter the Email", placeholder="Type Here")
        password = cols[1].text_input("Enter the Password", placeholder="Type here", type="password")
        if cols[1].checkbox("Login"):
            try:
                global result_login
                result_login = UserData.UserLogin(username, password)
                if type(result_login) == list and result_login[1] == "success":
                    st.success("Minimise the login for a better view and select the course from sidebar")
                    cols_menu = st.columns(3)
                    global course_menu
                    course_menu = st.sidebar.selectbox("Select the course", ["Animations", "Artificial Intelligence"])
                elif result_login[1] == "Pending":
                    st.warning("Your approval is pending from admin.")
                else:
                    st.sidebar.warning("Check the user credentials")
            except:
                st.markdown("")
try:
    if course_menu == "Animations":
        main_menu = option_menu("", ["My Profile", "Course Content", "Community Arena"],
                                icons=["person-fill", "journal-album", "chat-quote"], default_index=1,
                                styles={"nav-link-selected": {"background-color": "#0ea2bd"}}, orientation="horizontal")
        if main_menu == "My Profile":
            profile.display(profile_details=result_login[0],rating=result_login[0]["AnimationR"],rewards=result_login[0]["AnimationXp"])
            with st.expander("Appreciation by Instructors"):
                for i in result_login[0]["Appreciation"]:
                    st.markdown(i)
        if main_menu == "Community Arena":
            st.image("Images/coming-soon.png")
        if main_menu == "Course Content":
            with st.sidebar:
                menu = option_menu("Course menu", ['What do I learn', "Let's take good photos", "Basics of Photography",
                                                   "Stop motion studio", "My First Animation",
                                                   "Challenge : Create & Publish"],
                                   menu_icon="menu-button-fill",
                                   icons=["book-fill", "camera-fill", "card-image", "camera-reels-fill",
                                          "caret-right-square-fill", "cloud-upload-fill"], default_index=0,
                                   styles={"nav-link-selected": {"background-color": "#0ea2bd"}})
            if menu == "What do I learn":
                st.markdown("<h3 style='text-align:center; color: #0ea2bd;'>1. Learning outcomes</h3>",unsafe_allow_html=True)
                st.markdown("___")
                cols = st.columns([2, 5])
                cols[0].image("Images/learningoutcomes.png", width=220)
                cols[1].markdown("<h5>By the end of this module, you will learn: </h5>", unsafe_allow_html=True)
                cols[1].markdown(" 1. Fundamentals of photography - How to take good photos, shots, angles and scenes!")
                cols[1].markdown(" 2. How to use Stop motion studio app for creating animations!")
                cols[1].markdown(" 3. Create basic animations using sticky notes and clay.")
                cols[1].markdown(" 4. Edit and publish animation created, and share it with community.")
            if menu == "Let's take good photos":
                st.markdown("<h3 style='text-align:center; color: #0ea2bd;'>2. How to take good photos?</h3>",unsafe_allow_html=True)
                st.markdown("___")
                st.info("Activity 1 : Observe the following photos and figure out what did you think is wrong with the photos!")
                cols=st.columns([1,2,1,2,1])
                cols[1].image("Images/photography/blur.jpeg")
                cols[3].image("Images/photography/improper.jpeg")
                if st.checkbox("Check for solution"):
                    st.markdown("1. Image 1 is blurred that might happen due to bad lighting or camera is not geld still.")
                    st.markdown("2. Image 2 has multiple subjects and frame is not properly set.")
                    st.markdown("<h5 style='text-align:center; color: #0ea2bd;'>Now let's learn about things that need to be kept in mind in order to take good photos.</h5>",unsafe_allow_html=True)
                    st.markdown("1. Subject needs to be focused with obstacles removed around it.")
                    st.markdown("2. Frame needs to be defined to capture a subject.")
                    st.markdown("3. Good lighting and holding camera still is also required.")
                    st.markdown("4. Don't shoot with the light behind the subject.")
            if menu == "Basics of Photography":
                st.markdown("<h3 style='text-align:center; color: #0ea2bd;'>3. Let's make the picture perfect !</h3>",unsafe_allow_html=True)
                st.markdown("___")
                st.info("Activity 2 : Observe the following photos and understand what is being focused in each frame!")
                cols = st.columns([1,1])
                cols[0].markdown("The image has 5 different shots.")
                cols[0].image("Images/photography/shots.jpeg",use_column_width=True)
                if cols[1].checkbox("Click for solution"):
                    cols[1].markdown(
                        "<h5 style='text-align:center; color: #0ea2bd;'>Here is the description for each shot. </h5>",
                        unsafe_allow_html=True)
                    cols[1].markdown("1. Wide shot: focus is on setting and location for scene is established.")
                    cols[1].markdown("2. Long shot: focus is more on setting and less on subject's presence in setting.")
                    cols[1].markdown("3. Mid shot: focus is equal on setting and subject.")
                    cols[1].markdown("4. Medium close up shot: focus is less on setting and more on subject.")
                    cols[1].markdown("5. Close up shot: focus is only on subject.")
                    cols[1].image("Images/photography/shots_1.jpg", use_column_width=True)
                    st.info("Activity 3 : Try out the camera angles in below picture and discuss with your partner whether you got the results as demonstrated.!")
                    st.image("Images/photography/angles.png", use_column_width=True)
            if menu == "Stop motion studio":
                st.markdown("<h3 style='text-align:center; color: #0ea2bd;'>4. Let's set our devices ready for animations !</h3>",unsafe_allow_html=True)
                st.markdown("___")
                st.info("Activity 4 : Let's install and explore the software to start creating our animations.")
                st.markdown("1. Install the 'Stop Motion Studio' from the Appstore or Playstore or Windows store based on your device. Preview of the app on store is as shown below.")
                st.image("images/stopmotion/stopmotion1.jpeg")
                st.markdown("2. Open the app on the device which directs to below screen and click on Big Fish animation.")
                st.image("images/stopmotion/stopmotion2.jpeg")
                st.markdown("3. Click on play button ▶️ to watch the animation.")
                st.image("images/stopmotion/stopmotion3.jpeg")
                st.markdown("4. Click on help button❔️to know about other options on the screen. Try out each button and finally navigate to the initial screen of step 2.")
                st.image("images/stopmotion/stopmotion4.jpeg")
                st.markdown("5. Click on ... at the bottom of big fish animation for quick options that allows you to share or save the video.")
                st.image("images/stopmotion/stopmotion5.jpeg")
            if menu == "My First Animation":
                st.markdown("<h3 style='text-align:center; color: #0ea2bd;'>5. It's time to create our first animation.</h3>",unsafe_allow_html=True)
                st.markdown("___")
                st.info("Activity 5 : Watch the below videos to understand how the outputs of stop motion animation looks like!")
                cols = st.columns(2)
                cols[0].video("https://www.youtube.com/watch?v=RfopenHZ6EE")
                cols[1].video("https://www.youtube.com/watch?v=yGXhbYtYTWk&list=PLoR4NuvlhinuXeb501SJ2Q25sqRsCCx8r&index=5")
                st.info("Activity 6 : Now let's create a simple animation with objects around us by following the below steps.")
                cols_1 = st.columns([1.1,3])
                cols_1[1].markdown("1. Decide an object around you for creating motion in straight line.")
                cols_1[1].markdown("2. Open stop motion studio and click on new movie.")
                cols_1[1].markdown("3. Fix the camera focused on the object in a comfortable position.")
                cols_1[1].markdown("4. Start capturing the object by slightly moving the object after each frame is shot.")
                cols_1[1].markdown("5. Make sure you shoot atleast 100 frames for 10 sec animation. ")
                cols_1[1].markdown("6. The video on left side is a simple animation of toy movement.")
                cols_1[0].video("Images/stopmotion/animation.mp4")
            if menu == "Challenge : Create & Publish":
                st.markdown("<h3 style='text-align:center; color: #0ea2bd;'>6. Time for the challenge !</h3>",unsafe_allow_html=True)
                st.markdown("___")
                st.info("Challenge 1 : Create a stop motion animation on your own, edit it and upload the video to google form mentioned below.")
                st.markdown("Here are some instructions")
                st.markdown("1. Use any of the objects on table to create your animation - objects include mini toys sticky notes, clay and lego bricks.")
                st.markdown("2. Plan a small concept around the chosen object.")
                st.markdown("3. Decide the place to shoot and work with your partner to complete the task of shooting the frames.")
                st.markdown("4. Edit the movie - add credits, music or voice over to make your movie a masterpiece. Export the video to your device.")
                st.markdown("5. Click on the link below and upload the video with your details.")
                st.write("click here [Upload the animation](https://forms.gle/bjmSUJZbsgJu87jc8)")
    if course_menu == "Artificial Intelligence":
        main_menu = option_menu("", ["My Profile", "Course Content", "Community Arena"],
                                icons=["person-fill", "journal-album", "chat-quote"], default_index=1,
                                styles={"nav-link-selected": {"background-color": "#0ea2bd"}}, orientation="horizontal")
        if main_menu == "My Profile":
            profile.display(profile_details=result_login[0],rating=result_login[0]["AIR"],rewards=result_login[0]["AIXP"])
            with st.expander("Appreciation by Instructors"):
                for i in result_login[0]["Appreciation"]:
                    st.markdown(i)
        if main_menu == "Community Arena":
            st.image("Images/coming-soon.png")
        if main_menu == "Course Content":
            st.image("Images/coming-soon.png")
            st.info("But let's try to build an AI system before we end !")


except:
    st.markdown("")