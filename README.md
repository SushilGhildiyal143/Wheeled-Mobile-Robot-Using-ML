# Control of Wheeled Mobile Robot using Computer Vision
In today’s developing technology,
industries are playing important role for the
betterment of life and society. But in industries
many functions are running under hazardous
conditions, so demand of human free interaction
arises, which can be fulfilled by robotics. In
Chemical, Oil & Gas, Petrochemicals and many
manufacturing industries today we need human
safety on head, and it can be done by robots. This
paper implies such type of mobile robot which can
be used in complex industries. The work is based on
Image processing and Centroid Algorithm. The
physical quantities like (temperature, pressure,
humidity, stress, PH) and leakage of gases and
liquids, fire, spark and many human safety related
things which can be encountered by this mobile
robot. By using this robot, the main achievement is
human safety and simultaneously cost effective,
precision and all far away data can be easily
available through IoT (Cloud). Also, it works
without any disincentive at particular of desired
time in day or night, where particular place requires
physical quantities measurement. In this project the
main components are Controller (Raspberry Pi),
Four DC Motor for each wheel, Pi Camera for
image detection and processing, motor driver logic
and physical quantities sensor.

# METHODOLOGY
To attain this project centroid algorithm is
implemented so that the robot can follow the desired
path. This robot is mainly designed for hazardous
industry purpose. To get the data as well as pictures
at certain time so, by doing the time settings in
robot, it can automatically go and take the data at
that present time. This is accomplished using image
processing, at first video is converted in to frames
with format ‘BGR’ Image. The program is written
in language called Python i.e. high-level language.
Here, robot is design to follow black line, which is
denoted by Image= (0, 0, 0), (75, 75, 75). In GPIO
Board different pins are set for individual motors
that are attached to four wheels. From open
computer vision platform, erode command is used
for noise cancellation. The contour of black line is
detected using ‘find contours’ command [5].
Through this the angle of black line is detected i.e.
when the robot tilts right the angle is towards
negative and when the robot tilts left then the angle
is positive. After finding the contours the centroid
of the black line is measured. Therefore, by taking
centroid as a reference point, the angle is referred as
positive or negative.
The detection of path using camera captures is
shown in image. The bounded rectangle captures
the blackline in the numbers in red color shows the
angle between camera and blackline. When angle is
changed accordingly, output to motors also
changes.


# REFERENCES
[1] M. A. Putra, E. Pitowarno and A. Risnumawan, "Visual
servoing line following robot: Camera-based line detecting
and interpreting," 2017 International Electronics Symposium
on Engineering Technology and Applications (IES-ETA),
Surabaya, 2017, pp. 123-128.
[2] G. Antonelli, S. Chiaverini and G. Fusco, "Experiments of online
path following under joint limits for an industrial robot
manipulator," Proceedings of the International Conference on
Control Applications, Glasgow, UK, 2002, pp. 513-518 vol.1.
[3] J. Dupuis and M. Parizeau, "Evolving a Vision-Based Line-
Following Robot Controller," The 3rd Canadian Conference
on Computer and Robot Vision (CRV'06), 2006, pp. 75-75.doi:
10.1109/CRV.2006.32
[4] B. Song, Y. Zhang, J. Cheng and J. Wang, "Path Following
Control of a Mobile Robot via Line-of-Sight Method," 2010
Second International Conference on Intelligent Human-
Machine Systems and Cybernetics, Nanjing, Jiangsu, 2010, pp.
143-146.
[5] G. Sonal, P. Raninga and H. Patel, "Design and
implementation of RGB color line following robot," 2017
International Conference on Computing Methodologies and
Communication (ICCMC), Erode, 2017, pp. 442-446.
[6] K. Krinkin, E. Stotskaya and Y. Stotskiy, "Design and
implementation Raspberry Pi-based omni-wheel mobile
robot," 2015 Artificial Intelligence and Natural Language and
Information Extraction, Social Media and Web Search
FRUCT Conference (AINL-ISMW FRUCT), St. Petersburg,
2015, pp. 39-45.
[7] S. Saha et al., "GPS based smart spy surveillance robotic
system using Raspberry Pi for security application and remote
sensing," 2017 8th IEEE Annual Information Technology,
Electronics and Mobile Communication Conference
(IEMCON), Vancouver, BC, 2017, pp. 705-709.
doi: 10.1109/IEMCON.2017.8117239
[8] M. A. Gulzar, K. Kumar, M. A. Javed and M. Sharif, "Highvoltage
transmission line inspection robot," 2018
International Conference on Engineering and Emerging
Technologies (ICEET), Lahore, Pakistan, 2018, pp. 1-7.
doi: 10.1109/ICEET1.2018.8338632
[9] R. Neves and A. C. Matos, "Raspberry PI based stereo vision
for small size ASVs," 2013 OCEANS - San Diego, San Diego,
CA, 2013, pp. 1-6.
doi: 10.23919/OCEANS.2013.6741334
[10] S. Sruthy and S. N. George, "WiFi enabled home security
surveillance system using Raspberry Pi and IoT
module," 2017 IEEE International Conference on Signal
Processing, Informatics, Communication and Energy Systems
(SPICES), Kollam, 2017, pp. 1-6.
doi: 10.1109/SPICES.2017.8091320
[11] F. T. Espinoza, B. G. Gabriel and M. J. Barros, "Computer
vision classifier and platform for automatic counting: More
than cars," 2017 IEEE Second Ecuador Technical Chapters
Meeting (ETCM), Salinas, 2017, pp. 1-6.
doi: 10.1109/ETCM.2017.8247454
[12] M. Dragusu, A. N. Mihalache and R. Solea, "Practical
applications for robotic arms using image processing," 2012
16th International Conference on System Theory, Control and
Computing (ICSTCC), Sinaia, 2012, pp. 1-6.
[13] N. M. Vaidya and K. L. Boyer, "Stereopsis and image
registration from extended edge features in the absence of
camera pose information," Proceedings. 1991 IEEE Computer
Society Conference on Computer Vision and Pattern
Recognition, Maui, HI, 1991, pp. 76-82.
doi: 10.1109/CVPR.1991.139664
[14] M. D. Kim and J. Ueda, "Real-Time Panoramic Image
Generation and Motion Deblurring by Using Dynamics-Based
Robotic Vision," in IEEE/ASME Transactions on
Mechatronics, vol. 21, no. 3, pp. 1376-1387, June 2016.
doi: 10.1109/TMECH.2015.2511091
[15] S. H. Lee, J. Y. Choi, K. N. Plataniotis and Y. M. Ro, "Local
color vector binary pattern for face recognition," 2011 18th
IEEE International Conference on Image Processing, Brussels,
2011, pp. 2997-3000.
doi: 10.1109/ICIP.2011.6116292
[16] A.J. Nor'aini, M. H. Ahmad Faris and N. Haryanti, "Image
reconstruction: A comparison between moment and nonmoment
based techniques," 2011 IEEE International
Conference on Computer Applications and Industrial
Electronics (ICCAIE), Penang, 2011, pp. 361-366.
doi: 10.1109/ICCAIE.2011.6162161
[17] T. Ojala, M. Pietikainen and T. Maenpaa, "Multiresolution
gray-scale and rotation invariant texture classification with
local binary patterns," in IEEE Transactions on Pattern
Analysis and Machine Intelligence, vol. 24, no. 7, pp. 971-987,
Jul 2002.
doi: 10.1109/TPAMI.2002.1017623
[18] B. Horan, Z. Najdovski, T. Black, S. Nahavandi and P.
Crothers, "OzTug mobile robot for manufacturing
transportation," 2011 IEEE International Conference on
Systems, Man, and Cybernetics, Anchorage, AK, 2011, pp.
3554-3560.doi: 10.1109/ICSMC.2011.6084220
[19] Ignatev, Konstantin & N. Sheludko, V & V. Serykh, E & L.
Rusyaeva, T. (2017). Application of genetic algorithms in
adaptive control systems design. 386-388.
10.1109/SCM.2017.7970593.
[20] N. Sheludko, Viktor & Vl. Putov, Viktor & D. Stotckaia,
Anastasiia. (2015). Educational, scientific and innovative
potential mood of the control systems department in the
knowledge area of mechatronics & robotics. 11-13.
