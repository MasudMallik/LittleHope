import streamlit as st
import requests
if "login" not in st.session_state:
    st.session_state.login = True

def login():
        st.title("Login")
        email = st.text_input("Enter email", placeholder="email@gmail.com")
        password = st.text_input(
            "Enter password",
            placeholder="At least 1 uppercase, lowercase, special character, and digit",
            type="password"
        )

        col1, col2 = st.columns(2)

        if col1.button("Login", type="primary", use_container_width=True):
            if email and password:
                response = requests.post(
                    "http://127.0.0.1:8000/login",
                    json={"email": email, "password": password}
                )
                if response.status_code == 200:
        #             tok=response.json()
        #             st.session_state.token=tok["access_type"]+" "+tok["token"]
        #             res=requests.post( "http://127.0.0.1:8000/login",headers = {"Authorization": f"Bearer {st.session_state.token}"}
        # )
                    result=response.json()
                    if(result.get("login")==False):
                        st.info("you dont have an account please create it")
                    st.success(response.json())
                else:
                    st.error("Login failed ❌")
            else:
                st.warning("Please enter both email and password")

        if col2.button("New user", type="primary", use_container_width=True):
            st.session_state.login=False
            st.rerun()

def registration():
        states=["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]
        districts = {
    "Andhra Pradesh": [
        "Anantapur","Chittoor","East Godavari","Guntur","Krishna","Kurnool","Prakasam",
        "Sri Potti Sriramulu Nellore","Srikakulam","Visakhapatnam","Vizianagaram","West Godavari",
        "YSR Kadapa","Anakapalli","Bapatla","Konaseema","NTR","Palnadu","Parvathipuram Manyam",
        "Sri Sathya Sai","Tirupati","Alluri Sitharama Raju","Kakinada","Eluru","Nandyal"
    ],
    "Arunachal Pradesh": [
        "Tawang","West Kameng","East Kameng","Pakke-Kessang","Papum Pare","Kra Daadi","Kurung Kumey",
        "Lower Subansiri","Upper Subansiri","Kamle","Lower Siang","Upper Siang","West Siang","Shi-Yomi",
        "Leparada","East Siang","Dibang Valley","Lower Dibang Valley","Lohit","Anjaw","Namsai","Changlang",
        "Tirap","Longding","Siang","Itanagar Capital Complex"
    ],
    "Assam": [
        "Baksa","Barpeta","Biswanath","Bongaigaon","Cachar","Charaideo","Chirang","Darrang","Dhemaji",
        "Dhubri","Dibrugarh","Goalpara","Golaghat","Hailakandi","Hojai","Jorhat","Kamrup","Kamrup Metropolitan",
        "Karbi Anglong","Karimganj","Kokrajhar","Lakhimpur","Majuli","Morigaon","Nagaon","Nalbari","Sivasagar",
        "Sonitpur","South Salmara-Mankachar","Tinsukia","Udalguri","West Karbi Anglong","Bajali","Tamulpur"
    ],
    "Bihar": [
        "Araria","Arwal","Aurangabad","Banka","Begusarai","Bhagalpur","Bhojpur","Buxar","Darbhanga",
        "East Champaran","Gaya","Gopalganj","Jamui","Jehanabad","Kaimur","Katihar","Khagaria","Kishanganj",
        "Lakhisarai","Madhepura","Madhubani","Munger","Muzaffarpur","Nalanda","Nawada","Patna","Purnia",
        "Rohtas","Saharsa","Samastipur","Saran","Sheikhpura","Sheohar","Sitamarhi","Siwan","Supaul",
        "Vaishali","West Champaran"
    ],
    "Chhattisgarh": [
        "Balod","Baloda Bazar","Balrampur","Bastar","Bemetara","Bijapur","Bilaspur","Dantewada","Dhamtari",
        "Durg","Gariaband","Janjgir-Champa","Jashpur","Kabirdham","Kanker","Kondagaon","Korba","Koriya",
        "Mahasamund","Mungeli","Narayanpur","Raigarh","Raipur","Rajnandgaon","Sukma","Surajpur","Surguja",
        "Gaurela-Pendra-Marwahi","Manendragarh-Chirmiri-Bharatpur","Mohla-Manpur-Ambagarh Chowki",
        "Khairagarh-Chhuikhadan-Gandai","Sarangarh-Bilaigarh"
    ],
    "Goa": ["North Goa","South Goa"],
    "Gujarat": [
        "Ahmedabad","Amreli","Anand","Aravalli","Banaskantha","Bharuch","Bhavnagar","Botad","Chhota Udaipur",
        "Dahod","Dang","Devbhoomi Dwarka","Gandhinagar","Gir Somnath","Jamnagar","Junagadh","Kheda","Kutch",
        "Mahisagar","Mehsana","Morbi","Narmada","Navsari","Panchmahal","Patan","Porbandar","Rajkot",
        "Sabarkantha","Surat","Surendranagar","Tapi","Vadodara","Valsad"
    ],
    "Haryana": [
        "Ambala","Bhiwani","Charkhi Dadri","Faridabad","Fatehabad","Gurugram","Hisar","Jhajjar","Jind",
        "Kaithal","Karnal","Kurukshetra","Mahendragarh","Nuh","Palwal","Panchkula","Panipat","Rewari",
        "Rohtak","Sirsa","Sonipat","Yamunanagar"
    ],
    "Himachal Pradesh": [
        "Bilaspur","Chamba","Hamirpur","Kangra","Kinnaur","Kullu","Lahaul and Spiti","Mandi","Shimla",
        "Sirmaur","Solan","Una"
    ],
    "Jharkhand": [
        "Bokaro","Chatra","Deoghar","Dhanbad","Dumka","East Singhbhum","Garhwa","Giridih","Godda","Gumla",
        "Hazaribagh","Jamtara","Khunti","Koderma","Latehar","Lohardaga","Pakur","Palamu","Ramgarh","Ranchi",
        "Sahibganj","Saraikela Kharsawan","Simdega","West Singhbhum"
    ],
    "Karnataka": [
        "Bagalkot","Ballari","Belagavi","Bengaluru Rural","Bengaluru Urban","Bidar","Chamarajanagar",
        "Chikkaballapur","Chikkamagaluru","Chitradurga","Dakshina Kannada","Davanagere","Dharwad","Gadag",
        "Hassan","Haveri","Kalaburagi","Kodagu","Kolar","Koppal","Mandya","Mysuru","Raichur","Ramanagara",
        "Shivamogga","Tumakuru","Udupi","Uttara Kannada","Vijayapura","Yadgir"
    ],
    "Kerala": [
        "Alappuzha","Ernakulam","Idukki","Kannur","Kasaragod","Kollam","Kottayam","Kozhikode","Malappuram",
        "Palakkad","Pathanamthitta","Thiruvananthapuram","Thrissur","Wayanad"
    ],
    "Madhya Pradesh": [
        "Agar Malwa","Alirajpur","Anuppur","Ashoknagar","Balaghat","Barwani","Betul","Bhind","Bhopal",
        "Burhanpur","Chhatarpur","Chhindwara","Damoh","Datia","Dewas","Dhar","Dindori","Guna","Gwalior",
        "Harda","Hoshangabad","Indore","Jabalpur","Jhabua","Katni","Khandwa","Khargone","Mandla","Mandsaur",
        "Morena","Narsinghpur","Neemuch","Panna","Raisen","Rajgarh","Ratlam","Rewa","Sagar","Satna","Sehore",
        "Seoni","Shahdol","Shajapur","Sheopur","Shivpuri","Sidhi","Singrauli","Tikamgarh","Ujjain","Umaria",
        "Vidisha"
    ],
    "Maharashtra": [
        "Ahmednagar","Akola","Amravati","Aurangabad","Beed","Bhandara","Buldhana","Chandrapur","Dhule",
        "Gadchiroli","Gondia","Hingoli","Jalgaon","Jalna","Kolhapur","Latur","Mumbai City","Mumbai Suburban",
        "Nagpur","Nanded","Nandurbar","Nashik","Osmanabad","Palghar","Parbhani","Pune","Raigad","Ratnagiri",
        "Sangli","Satara","Sindhudurg","Solapur","Thane","Wardha","Washim","Yavatmal"
    ],
    "Manipur": [
        "Bishnupur","Chandel","Churachandpur","Imphal East","Imphal West","Jiribam","Kakching","Kamjong",
        "Kangpokpi","Noney","Pherzawl","Senapati","Tamenglong","Tengnoupal","Thoubal","Ukhrul"
    ],
    "Meghalaya": [
        "East Garo Hills","East Jaintia Hills","East Khasi Hills","North Garo Hills","Ri-Bhoi","South Garo Hills",
        "South West Garo Hills","South West Khasi Hills","West Garo Hills","West Jaintia Hills","West Khasi Hills"
    ],
    "Mizoram": [
        "Aizawl","Champhai","Hnahthial","Khawzawl","Kolasib","Lawngtlai","Lunglei","Mamit","Saiha","Saitual",
        "Serchhip"
    ],
    "Nagaland": [
        "Chümoukedima","Dimapur","Kiphire","Kohima","Longleng","Mokokchung","Mon","Niuland","Noklak","Peren",
        "Phek","Shamator","Tuensang","Tseminyu","Wokha","Zünheboto"
    ],
    "Odisha": [
        "Angul","Balangir","Balasore","Bargarh","Bhadrak","Boudh","Cuttack","Deogarh","Dhenkanal","Gajapati",
        "Ganjam","Jagatsinghpur","Jajpur","Jharsuguda","Kalahandi","Kandhamal","Kendrapara","Keonjhar","Khordha",
        "Koraput","Malkangiri","Mayurbhanj","Nabarangpur","Nayagarh","Nuapada","Puri","Rayagada","Sambalpur",
        "Subarnapur","Sundargarh"
    ],
    "Punjab": [
        "Amritsar","Barnala","Bathinda","Faridkot","Fatehgarh Sahib","Fazilka","Ferozepur","Gurdaspur","Hoshiarpur",
        "Jalandhar","Kapurthala","Ludhiana","Malerkotla","Mansa","Moga","Mohali","Muktsar","Pathankot","Patiala",
        "Rupnagar","Sangrur","Shaheed Bhagat Singh Nagar","Tarn Taran"
    ],
    "Rajasthan": [
        "Ajmer","Alwar","Banswara","Baran","Barmer","Bharatpur","Bhilwara","Bikaner","Bundi","Chittorgarh",
        "Churu","Dausa","Dholpur","Dungarpur","Hanumangarh","Jaipur","Jaisalmer","Jalore","Jhalawar","Jhunjhunu",
        "Jodhpur","Karauli","Kota","Nagaur","Pali","Pratapgarh","Rajsamand","Sawai Madhopur","Sikar","Sirohi",
        "Sri Ganganagar","Tonk","Udaipur"
    ],
    "Sikkim": ["East Sikkim","North Sikkim","South Sikkim","West Sikkim"],
    "Tamil Nadu": [
        "Ariyalur","Chengalpattu","Chennai","Coimbatore","Cuddalore","Dharmapuri","Dindigul","Erode","Kallakurichi",
        "Kanchipuram","Kanyakumari","Karur","Krishnagiri","Madurai","Nagapattinam","Namakkal","Nilgiris","Perambalur",
        "Pudukkottai","Ramanathapuram","Ranipet","Salem","Sivaganga","Tenkasi","Thanjavur","Theni","Thoothukudi",
        "Tiruchirappalli","Tirunelveli","Tirupathur","Tiruppur","Tiruvallur","Tiruvannamalai","Tiruvarur","Vellore",
        "Viluppuram","Virudhunagar"
    ],
    "Telangana": [
        "Adilabad","Bhadradri Kothagudem","Hanamkonda","Hyderabad","Jagtial","Jangaon","Jayashankar Bhupalpally",
        "Jogulamba Gadwal","Kamareddy","Karimnagar","Khammam","Komaram Bheem Asifabad","Mahabubabad","Mahabubnagar",
        "Mancherial","Medak","Medchal-Malkajgiri","Mulugu","Nagarkurnool","Nalgonda","Narayanpet","Nirmal","Nizamabad",
        "Peddapalli","Rajanna Sircilla","Ranga Reddy","Sangareddy","Siddipet","Suryapet","Vikarabad","Wanaparthy",
        "Warangal","Yadadri Bhuvanagiri"
    ],
    "Tripura": [
        "Dhalai","Gomati","Khowai","North Tripura","Sepahijala","South Tripura","Unakoti","West Tripura"
    ],
    "Uttar Pradesh": [
        "Agra","Aligarh","Ambedkar Nagar","Amethi","Amroha","Auraiya","Ayodhya","Azamgarh","Baghpat","Bahraich",
        "Ballia","Balrampur","Banda","Barabanki","Bareilly","Basti","Bhadohi","Bijnor","Budaun","Bulandshahr",
        "Chandauli","Chitrakoot","Deoria","Etah","Etawah","Farrukhabad","Fatehpur","Firozabad","Gautam Buddha Nagar",
        "Ghaziabad","Ghazipur","Gonda","Gorakhpur","Hamirpur","Hapur","Hardoi","Hathras","Jalaun","Jaunpur","Jhansi",
        "Kannauj","Kanpur Dehat","Kanpur Nagar","Kasganj","Kaushambi","Kheri","Kushinagar","Lalitpur","Lucknow",
        "Maharajganj","Mahoba","Mainpuri","Mathura","Mau","Meerut","Mirzapur","Moradabad","Muzaffarnagar","Pilibhit",
        "Pratapgarh","Prayagraj","Raebareli","Rampur","Saharanpur","Sambhal","Sant Kabir Nagar","Shahjahanpur",
        "Shamli","Shravasti","Siddharthnagar","Sitapur","Sonbhadra","Sultanpur","Unnao","Varanasi"
    ],
    "Uttarakhand": [
        "Almora","Bageshwar","Chamoli","Champawat","Dehradun","Haridwar","Nainital","Pauri Garhwal","Pithoragarh",
        "Rudraprayag","Tehri Garhwal","Udham Singh Nagar","Uttarkashi"
    ],
    "West Bengal": [
        "Alipurduar","Bankura","Birbhum","Cooch Behar","Dakshin Dinajpur","Darjeeling","Hooghly","Howrah",
        "Jalpaiguri","Jhargram","Kalimpong","Kolkata","Malda","Murshidabad","Nadia","North 24 Parganas","Paschim Bardhaman","Paschim Medinipur","Purba Bardhaman","Purba Medinipur","Purulia","South 24 Parganas","Uttar Dinajpur"]}
       
        st.title("Registration")
        st.text("Enter your Details properly: ")
        st.divider()
        name=st.text_input(label="Enter your full name: ",placeholder="Abc Def")
        email=st.text_input(label="Enter your email-Id: ",placeholder="email@gmail.com",)
        contact_no=st.text_input(label="Enter your contact number: ",placeholder="123XXXXXXX")
        state=st.selectbox("Choose your state: ",list(states))
        district=st.selectbox("Choose your District ",["choose"]+list(districts[state]))
        password = st.text_input(
            "Enter password",
            placeholder="At least 1 uppercase, 1 lowercase,1 special character, and 1 digit",
            type="password",
        )
        confirm_password = st.text_input(
            "Confirm password",
            placeholder="At least 1 uppercase, 1 lowercase,1 special character, and 1 digit",
            type="password"
        )
        col1, col2 = st.columns(2)

        if col2.button("Already have an account", type="primary", use_container_width=True):
            st.session_state.login=True
            st.rerun()
        if col1.button("Registration", type="primary", use_container_width=True):
                st.session_state.clear()
                response=requests.post("http://127.0.0.1:8000/register",
                json={
                    "name":name,
                    "email":email,
                    "contact_no":contact_no,
                    "state":state,
                    "district":district,
                    "password":password
                })
                st.write(response.status_code)
                if response.status_code == 200:
                    data = response.json()
                    st.session_state.user_details = data

                    if data.get("user_details") == "True":
                        st.info("You already have an account, please login...")
                    else:
                                st.success("Successfully logged in")
                                st.switch_page("pages/report_child.py")
                err=response.json()
                if "detail" in err:
                     for error in err["detail"]:
                          st.write(error["msg"])
             


if st.session_state.login==True:
    c=login()
else:
    c=registration()