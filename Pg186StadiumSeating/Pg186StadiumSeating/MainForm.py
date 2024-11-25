import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._groupBox1.SuspendLayout()
        self._groupBox2.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
        self._groupBox1.Controls.Add(self._textBox3)
        self._groupBox1.Controls.Add(self._textBox2)
        self._groupBox1.Controls.Add(self._textBox1)
        self._groupBox1.Controls.Add(self._label4)
        self._groupBox1.Controls.Add(self._label3)
        self._groupBox1.Controls.Add(self._label2)
        self._groupBox1.Controls.Add(self._label1)
        self._groupBox1.Font = System.Drawing.Font("Gill Sans MT Condensed", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.ForeColor = System.Drawing.Color.Red
        self._groupBox1.Location = System.Drawing.Point(12, 12)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(285, 216)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Tickets Sold"
        # 
        # groupBox2
        # 
        self._groupBox2.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
        self._groupBox2.Controls.Add(self._label12)
        self._groupBox2.Controls.Add(self._label11)
        self._groupBox2.Controls.Add(self._label10)
        self._groupBox2.Controls.Add(self._label8)
        self._groupBox2.Controls.Add(self._label6)
        self._groupBox2.Controls.Add(self._label5)
        self._groupBox2.Controls.Add(self._label9)
        self._groupBox2.Controls.Add(self._label7)
        self._groupBox2.Font = System.Drawing.Font("Gill Sans MT Condensed", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox2.ForeColor = System.Drawing.Color.Red
        self._groupBox2.Location = System.Drawing.Point(320, 12)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.RightToLeft = System.Windows.Forms.RightToLeft.Yes
        self._groupBox2.Size = System.Drawing.Size(285, 216)
        self._groupBox2.TabIndex = 1
        self._groupBox2.TabStop = False
        self._groupBox2.Text = "Revenue Generated"
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Gill Sans MT Condensed", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(47, 26)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(232, 56)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter the number of tickets sold for each class of seats"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Gill Sans MT Condensed", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(47, 90)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(232, 29)
        self._label2.TabIndex = 1
        self._label2.Text = "Class A:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Gill Sans MT Condensed", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(47, 124)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(232, 29)
        self._label3.TabIndex = 2
        self._label3.Text = "Class B:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Gill Sans MT Condensed", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(47, 157)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(232, 29)
        self._label4.TabIndex = 3
        self._label4.Text = "Class C:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
        self._textBox1.Font = System.Drawing.Font("Gill Sans MT Condensed", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(105, 90)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(164, 27)
        self._textBox1.TabIndex = 4
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
        self._textBox2.Font = System.Drawing.Font("Gill Sans MT Condensed", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(105, 124)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(164, 27)
        self._textBox2.TabIndex = 5
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
        self._textBox3.Font = System.Drawing.Font("Gill Sans MT Condensed", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(105, 157)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(164, 27)
        self._textBox3.TabIndex = 6
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Gill Sans MT Condensed", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(44, 113)
        self._label5.Name = "label5"
        self._label5.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label5.Size = System.Drawing.Size(232, 29)
        self._label5.TabIndex = 9
        self._label5.Text = "Class C:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Gill Sans MT Condensed", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(44, 80)
        self._label6.Name = "label6"
        self._label6.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label6.Size = System.Drawing.Size(232, 29)
        self._label6.TabIndex = 8
        self._label6.Text = "Class B:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("Gill Sans MT Condensed", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(44, 46)
        self._label7.Name = "label7"
        self._label7.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label7.Size = System.Drawing.Size(232, 29)
        self._label7.TabIndex = 7
        self._label7.Text = "Class A:"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label8
        # 
        self._label8.Font = System.Drawing.Font("Gill Sans MT Condensed", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(9, 145)
        self._label8.Name = "label8"
        self._label8.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label8.Size = System.Drawing.Size(267, 29)
        self._label8.TabIndex = 13
        self._label8.Text = "Total Revenue:"
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Ivory
        self._button1.Font = System.Drawing.Font("Gill Sans MT Condensed", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Red
        self._button1.Location = System.Drawing.Point(97, 251)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(137, 53)
        self._button1.TabIndex = 2
        self._button1.Text = "Calculate Revenue"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Ivory
        self._button2.Font = System.Drawing.Font("Gill Sans MT Condensed", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Red
        self._button2.Location = System.Drawing.Point(240, 251)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(137, 53)
        self._button2.TabIndex = 3
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Tomato
        self._button3.Font = System.Drawing.Font("Gill Sans MT Condensed", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.DarkRed
        self._button3.Location = System.Drawing.Point(383, 251)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(137, 53)
        self._button3.TabIndex = 4
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label9
        # 
        self._label9.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label9.Font = System.Drawing.Font("Gill Sans MT Condensed", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.ForeColor = System.Drawing.Color.Black
        self._label9.Location = System.Drawing.Point(102, 46)
        self._label9.Name = "label9"
        self._label9.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label9.Size = System.Drawing.Size(164, 27)
        self._label9.TabIndex = 15
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label10
        # 
        self._label10.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label10.Font = System.Drawing.Font("Gill Sans MT Condensed", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.ForeColor = System.Drawing.Color.Black
        self._label10.Location = System.Drawing.Point(102, 80)
        self._label10.Name = "label10"
        self._label10.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label10.Size = System.Drawing.Size(164, 27)
        self._label10.TabIndex = 16
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label11
        # 
        self._label11.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label11.Font = System.Drawing.Font("Gill Sans MT Condensed", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.ForeColor = System.Drawing.Color.Black
        self._label11.Location = System.Drawing.Point(102, 113)
        self._label11.Name = "label11"
        self._label11.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label11.Size = System.Drawing.Size(164, 27)
        self._label11.TabIndex = 17
        self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label12
        # 
        self._label12.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label12.Font = System.Drawing.Font("Gill Sans MT Condensed", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.ForeColor = System.Drawing.Color.Black
        self._label12.Location = System.Drawing.Point(102, 145)
        self._label12.Name = "label12"
        self._label12.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label12.Size = System.Drawing.Size(164, 27)
        self._label12.TabIndex = 18
        self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LimeGreen
        self.ClientSize = System.Drawing.Size(617, 331)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._groupBox1)
        self.Controls.Add(self._groupBox2)
        self.Name = "MainForm"
        self.Text = "Pg186StadiumSeating"
        self._groupBox1.ResumeLayout(False)
        self._groupBox1.PerformLayout()
        self._groupBox2.ResumeLayout(False)
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        aseats = float(self._textBox1.Text)
        bseats = float(self._textBox2.Text)
        cseats = float(self._textBox3.Text)
        acost = 15
        bcost = 12
        ccost = 9 
        arev = aseats * acost
        brev = bseats * bcost
        crev = cseats * ccost
        self._label9.Text = "$ " + str(arev)
        self._label10.Text = "$ " + str(brev)
        self._label11.Text = "$ " + str(crev)
        rev = arev + brev + crev
        self._label12.Text = "$ " + str(rev)

    def Button2Click(self, sender, e):
        self._label9.Text = ""
        self._label10.Text = ""
        self._label11.Text = ""
        self._label12.Text = ""
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()