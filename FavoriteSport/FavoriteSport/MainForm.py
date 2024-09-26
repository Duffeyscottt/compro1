import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label2 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self._label15 = System.Windows.Forms.Label()
        self._label16 = System.Windows.Forms.Label()
        self._label17 = System.Windows.Forms.Label()
        self._label19 = System.Windows.Forms.Label()
        self._label20 = System.Windows.Forms.Label()
        self._label21 = System.Windows.Forms.Label()
        self._label22 = System.Windows.Forms.Label()
        self._label23 = System.Windows.Forms.Label()
        self._label24 = System.Windows.Forms.Label()
        self._label25 = System.Windows.Forms.Label()
        self._label18 = System.Windows.Forms.Label()
        self._label27 = System.Windows.Forms.Label()
        self._label28 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label29 = System.Windows.Forms.Label()
        self._label26 = System.Windows.Forms.Label()
        self._label30 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 40, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label2.Location = System.Drawing.Point(372, 40)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(10, 101)
        self._label2.TabIndex = 1
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label2.Click += self.Label2Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Location = System.Drawing.Point(306, 67)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(10, 51)
        self._label1.TabIndex = 2
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.White
        self._label3.Location = System.Drawing.Point(300, 116)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(10, 20)
        self._label3.TabIndex = 3
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Location = System.Drawing.Point(313, 116)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(10, 20)
        self._label4.TabIndex = 4
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Black
        self._label5.Location = System.Drawing.Point(316, 91)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(32, 50)
        self._label5.TabIndex = 5
        self._label5.Click += self.Label5Click
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.Black
        self._label6.Location = System.Drawing.Point(274, 90)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(32, 50)
        self._label6.TabIndex = 6
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.Black
        self._label7.Location = System.Drawing.Point(291, 41)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(32, 50)
        self._label7.TabIndex = 7
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.White
        self._label8.Location = System.Drawing.Point(304, 81)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(16, 10)
        self._label8.TabIndex = 8
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.White
        self._label9.Location = System.Drawing.Point(283, 94)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(23, 10)
        self._label9.TabIndex = 9
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.Black
        self._label10.Location = System.Drawing.Point(283, 98)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(23, 10)
        self._label10.TabIndex = 10
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.White
        self._label11.Location = System.Drawing.Point(250, 92)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(16, 10)
        self._label11.TabIndex = 11
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.Black
        self._label12.Location = System.Drawing.Point(261, 97)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(23, 10)
        self._label12.TabIndex = 13
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.Color.White
        self._label13.Location = System.Drawing.Point(261, 95)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(23, 10)
        self._label13.TabIndex = 12
        # 
        # label14
        # 
        self._label14.BackColor = System.Drawing.Color.White
        self._label14.Location = System.Drawing.Point(411, 87)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(16, 10)
        self._label14.TabIndex = 23
        # 
        # label15
        # 
        self._label15.BackColor = System.Drawing.Color.Black
        self._label15.Location = System.Drawing.Point(422, 92)
        self._label15.Name = "label15"
        self._label15.Size = System.Drawing.Size(23, 10)
        self._label15.TabIndex = 25
        # 
        # label16
        # 
        self._label16.BackColor = System.Drawing.Color.White
        self._label16.Location = System.Drawing.Point(422, 90)
        self._label16.Name = "label16"
        self._label16.Size = System.Drawing.Size(23, 10)
        self._label16.TabIndex = 24
        # 
        # label17
        # 
        self._label17.BackColor = System.Drawing.Color.Black
        self._label17.Location = System.Drawing.Point(426, 81)
        self._label17.Name = "label17"
        self._label17.Size = System.Drawing.Size(23, 10)
        self._label17.TabIndex = 22
        # 
        # label19
        # 
        self._label19.BackColor = System.Drawing.Color.White
        self._label19.Location = System.Drawing.Point(446, 69)
        self._label19.Name = "label19"
        self._label19.Size = System.Drawing.Size(16, 10)
        self._label19.TabIndex = 20
        # 
        # label20
        # 
        self._label20.BackColor = System.Drawing.Color.Black
        self._label20.Location = System.Drawing.Point(435, 29)
        self._label20.Name = "label20"
        self._label20.Size = System.Drawing.Size(32, 50)
        self._label20.TabIndex = 19
        # 
        # label21
        # 
        self._label21.BackColor = System.Drawing.Color.Black
        self._label21.Location = System.Drawing.Point(418, 78)
        self._label21.Name = "label21"
        self._label21.Size = System.Drawing.Size(32, 58)
        self._label21.TabIndex = 18
        # 
        # label22
        # 
        self._label22.BackColor = System.Drawing.Color.Black
        self._label22.Location = System.Drawing.Point(460, 79)
        self._label22.Name = "label22"
        self._label22.Size = System.Drawing.Size(32, 62)
        self._label22.TabIndex = 17
        # 
        # label23
        # 
        self._label23.BackColor = System.Drawing.Color.White
        self._label23.Location = System.Drawing.Point(457, 114)
        self._label23.Name = "label23"
        self._label23.Size = System.Drawing.Size(10, 20)
        self._label23.TabIndex = 16
        # 
        # label24
        # 
        self._label24.BackColor = System.Drawing.Color.White
        self._label24.Location = System.Drawing.Point(444, 114)
        self._label24.Name = "label24"
        self._label24.Size = System.Drawing.Size(10, 20)
        self._label24.TabIndex = 15
        # 
        # label25
        # 
        self._label25.BackColor = System.Drawing.Color.White
        self._label25.Location = System.Drawing.Point(450, 55)
        self._label25.Name = "label25"
        self._label25.Size = System.Drawing.Size(10, 59)
        self._label25.TabIndex = 14
        # 
        # label18
        # 
        self._label18.BackColor = System.Drawing.Color.Black
        self._label18.Font = System.Drawing.Font("Microsoft Sans Serif", 45)
        self._label18.ForeColor = System.Drawing.Color.White
        self._label18.ImageAlign = System.Drawing.ContentAlignment.TopLeft
        self._label18.Location = System.Drawing.Point(313, -26)
        self._label18.Name = "label18"
        self._label18.Size = System.Drawing.Size(70, 65)
        self._label18.TabIndex = 26
        self._label18.Text = "."
        # 
        # label27
        # 
        self._label27.AccessibleName = ""
        self._label27.BackColor = System.Drawing.Color.Black
        self._label27.Font = System.Drawing.Font("Segoe Marker", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label27.ForeColor = System.Drawing.Color.White
        self._label27.Location = System.Drawing.Point(2, 1)
        self._label27.Name = "label27"
        self._label27.Size = System.Drawing.Size(283, 78)
        self._label27.TabIndex = 28
        self._label27.Text = "Favorite Sport"
        # 
        # label28
        # 
        self._label28.AccessibleName = ""
        self._label28.BackColor = System.Drawing.Color.Black
        self._label28.Font = System.Drawing.Font("Segoe Marker", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label28.ForeColor = System.Drawing.Color.White
        self._label28.Location = System.Drawing.Point(451, 63)
        self._label28.Name = "label28"
        self._label28.Size = System.Drawing.Size(283, 78)
        self._label28.TabIndex = 30
        self._label28.TextAlign = System.Drawing.ContentAlignment.BottomRight
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Black
        self._button1.Font = System.Drawing.Font("Segoe Marker", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.White
        self._button1.Location = System.Drawing.Point(12, 88)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(84, 42)
        self._button1.TabIndex = 31
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Black
        self._button2.Font = System.Drawing.Font("Segoe Marker", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.White
        self._button2.Location = System.Drawing.Point(582, 12)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(69, 38)
        self._button2.TabIndex = 32
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Black
        self._button3.Font = System.Drawing.Font("Segoe Marker", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.White
        self._button3.Location = System.Drawing.Point(657, 12)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(69, 38)
        self._button3.TabIndex = 33
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label29
        # 
        self._label29.AccessibleName = ""
        self._label29.BackColor = System.Drawing.Color.Black
        self._label29.Location = System.Drawing.Point(176, 145)
        self._label29.Name = "label29"
        self._label29.Size = System.Drawing.Size(403, 132)
        self._label29.TabIndex = 34
        # 
        # label26
        # 
        self._label26.AccessibleName = ""
        self._label26.BackColor = System.Drawing.Color.Black
        self._label26.Location = System.Drawing.Point(183, 9)
        self._label26.Name = "label26"
        self._label26.Size = System.Drawing.Size(403, 132)
        self._label26.TabIndex = 29
        # 
        # label30
        # 
        self._label30.AccessibleName = ""
        self._label30.BackColor = System.Drawing.Color.Black
        self._label30.Font = System.Drawing.Font("Segoe Marker", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label30.ForeColor = System.Drawing.Color.White
        self._label30.Location = System.Drawing.Point(2, 40)
        self._label30.Name = "label30"
        self._label30.Size = System.Drawing.Size(283, 45)
        self._label30.TabIndex = 35
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ControlText
        self.ClientSize = System.Drawing.Size(738, 142)
        self.Controls.Add(self._label30)
        self.Controls.Add(self._label29)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label28)
        self.Controls.Add(self._label26)
        self.Controls.Add(self._label27)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._label15)
        self.Controls.Add(self._label16)
        self.Controls.Add(self._label17)
        self.Controls.Add(self._label19)
        self.Controls.Add(self._label20)
        self.Controls.Add(self._label21)
        self.Controls.Add(self._label22)
        self.Controls.Add(self._label23)
        self.Controls.Add(self._label24)
        self.Controls.Add(self._label25)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label18)
        self.Name = "MainForm"
        self.Text = "FavoriteSport"
        self.ResumeLayout(False)


    def Label2Click(self, sender, e):
        pass

    def Label5Click(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button1Click(self, sender, e):
        self._label26.Location = System.Drawing.Point(176, 145)
        self._label30.Text = "Badminton"

    def Button2Click(self, sender, e):
        self._label26.Location = System.Drawing.Point(183, 9)
        self._label30.Text = " "