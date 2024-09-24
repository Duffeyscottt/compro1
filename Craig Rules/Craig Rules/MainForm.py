import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.LightSkyBlue
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 37, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(37, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(311, 94)
        self._label1.TabIndex = 0
        self._label1.Text = " "
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(12, 254)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(75, 23)
        self._button1.TabIndex = 1
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 8, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(0, -20)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(393, 19)
        self._button2.TabIndex = 2
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(148, 254)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(75, 23)
        self._button3.TabIndex = 3
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.Location = System.Drawing.Point(307, 254)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(75, 23)
        self._button4.TabIndex = 4
        self._button4.Text = "Exit"
        self._button4.UseVisualStyleBackColor = True
        self._button4.Click += self.Button4Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.LightSkyBlue
        self._label2.Location = System.Drawing.Point(13, 187)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 5
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.LightSkyBlue
        self._label3.Location = System.Drawing.Point(162, 121)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 6
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.LightSkyBlue
        self._label4.Location = System.Drawing.Point(-2, 121)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(100, 23)
        self._label4.TabIndex = 7
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.LightSkyBlue
        self._label5.Location = System.Drawing.Point(100, 156)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(100, 23)
        self._label5.TabIndex = 8
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.LightSkyBlue
        self._label6.Location = System.Drawing.Point(176, 187)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(100, 23)
        self._label6.TabIndex = 9
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.LightSkyBlue
        self._label7.Location = System.Drawing.Point(282, 187)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(100, 23)
        self._label7.TabIndex = 10
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label7.Click += self.Label7Click
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.LightSkyBlue
        self._label8.Location = System.Drawing.Point(100, 228)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(100, 23)
        self._label8.TabIndex = 11
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.LightSkyBlue
        self._label9.Location = System.Drawing.Point(292, 121)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(100, 23)
        self._label9.TabIndex = 12
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.LightSkyBlue
        self._label10.Location = System.Drawing.Point(282, 228)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(100, 23)
        self._label10.TabIndex = 13
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LightSkyBlue
        self.ClientSize = System.Drawing.Size(394, 289)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Craig Rules"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "Craig Rules!"
        self._button2.Location = System.Drawing.Point(0, 0)
        self._button2.Text = "confetti time"

    def Button4Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._label2.Text = "*confetti*"
        self._label3.Text = "*confetti*"
        self._label4.Text = "*confetti*"
        self._label5.Text = "*confetti*"
        self._label6.Text = "*confetti*"
        self._label7.Text = "*confetti*"
        self._label8.Text = "*confetti*"
        self._label9.Text = "*confetti*"
        self._label10.Text = "*confetti*"

    def Label7Click(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        self._label2.Text = " "
        self._label3.Text = " "
        self._label4.Text = " "
        self._label5.Text = " "
        self._label6.Text = " "
        self._label7.Text = " "
        self._label8.Text = " "
        self._label9.Text = " "
        self._label10.Text = " "
        self._label1.Text = " "
        self._button2.Location = System.Drawing.Point(0, -20)