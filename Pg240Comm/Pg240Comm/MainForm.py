import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(160, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 20)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(160, 38)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 20)
        self._textBox2.TabIndex = 1
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Lavender
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.Location = System.Drawing.Point(160, 106)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 2
        self._label1.Text = "label1"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Lavender
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label2.Location = System.Drawing.Point(160, 137)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 3
        self._label2.Text = "label2"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Lavender
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label3.Location = System.Drawing.Point(160, 167)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 4
        self._label3.Text = "label3"
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(45, 9)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(109, 23)
        self._label4.TabIndex = 5
        self._label4.Text = "Sales for the month:"
        # 
        # label5
        # 
        self._label5.Location = System.Drawing.Point(30, 38)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(124, 23)
        self._label5.TabIndex = 6
        self._label5.Text = "Advance pay awarded:"
        # 
        # label6
        # 
        self._label6.Location = System.Drawing.Point(30, 106)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(100, 23)
        self._label6.TabIndex = 7
        self._label6.Text = "Comission rate:"
        # 
        # label7
        # 
        self._label7.Location = System.Drawing.Point(30, 138)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(100, 23)
        self._label7.TabIndex = 8
        self._label7.Text = "Commissions:"
        # 
        # label8
        # 
        self._label8.Location = System.Drawing.Point(30, 168)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(100, 23)
        self._label8.TabIndex = 9
        self._label8.Text = "Net pay:"
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(27, 237)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(75, 23)
        self._button1.TabIndex = 10
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(108, 237)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(75, 23)
        self._button2.TabIndex = 11
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._button3.Location = System.Drawing.Point(189, 237)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(75, 23)
        self._button3.TabIndex = 12
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.AliceBlue
        self.ClientSize = System.Drawing.Size(292, 280)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Pg240Comm"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._label1.Text = ""
        self._label2.Text = ""
        self._label3.Text = ""
        self._textBox1.Text = ""
        self._textBox2.Text = ""