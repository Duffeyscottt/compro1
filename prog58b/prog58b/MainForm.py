import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.Highlight
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.Font = System.Drawing.Font("Engravers MT", 27, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(582, 45)
        self._label1.TabIndex = 0
        self._label1.Text = "Ax^2 + Bx + C"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.Highlight
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label2.Font = System.Drawing.Font("Engravers MT", 27, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label2.Location = System.Drawing.Point(284, 64)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(164, 45)
        self._label2.TabIndex = 1
        self._label2.Text = "A = "
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.White
        self._textBox1.Font = System.Drawing.Font("Engravers MT", 27, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.ForeColor = System.Drawing.Color.Teal
        self._textBox1.Location = System.Drawing.Point(371, 64)
        self._textBox1.Multiline = True
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(77, 45)
        self._textBox1.TabIndex = 2
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.White
        self._textBox2.Font = System.Drawing.Font("Engravers MT", 27, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.ForeColor = System.Drawing.Color.Teal
        self._textBox2.Location = System.Drawing.Point(371, 127)
        self._textBox2.Multiline = True
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(77, 45)
        self._textBox2.TabIndex = 4
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.Highlight
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label3.Font = System.Drawing.Font("Engravers MT", 27, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label3.Location = System.Drawing.Point(284, 127)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(164, 45)
        self._label3.TabIndex = 3
        self._label3.Text = "B = "
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.White
        self._textBox3.Font = System.Drawing.Font("Engravers MT", 27, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.ForeColor = System.Drawing.Color.Teal
        self._textBox3.Location = System.Drawing.Point(371, 187)
        self._textBox3.Multiline = True
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(77, 45)
        self._textBox3.TabIndex = 6
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.Highlight
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label4.Font = System.Drawing.Font("Engravers MT", 27, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label4.Location = System.Drawing.Point(284, 187)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(164, 45)
        self._label4.TabIndex = 5
        self._label4.Text = "C = "
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Silver
        self._button1.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(64, 64, 64)
        self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button1.Font = System.Drawing.Font("Engravers MT", 17, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.FromArgb(192, 0, 0)
        self._button1.Location = System.Drawing.Point(454, 64)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(140, 45)
        self._button1.TabIndex = 7
        self._button1.Text = "Exit"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightBlue
        self._button2.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(64, 64, 64)
        self._button2.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button2.Font = System.Drawing.Font("Engravers MT", 13, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.FromArgb(64, 64, 64)
        self._button2.Location = System.Drawing.Point(454, 127)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(140, 45)
        self._button2.TabIndex = 8
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.LightBlue
        self._button3.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(64, 64, 64)
        self._button3.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button3.Font = System.Drawing.Font("Engravers MT", 10, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.FromArgb(64, 64, 64)
        self._button3.Location = System.Drawing.Point(454, 187)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(140, 45)
        self._button3.TabIndex = 9
        self._button3.Text = "Calculate"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(0, 0, 64)
        self._label5.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label5.Font = System.Drawing.Font("Engravers MT", 27, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label5.Location = System.Drawing.Point(12, 64)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(266, 194)
        self._label5.TabIndex = 10
        self._label5.Text = "x = "
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FromArgb(0, 0, 64)
        self._label6.Font = System.Drawing.Font("Engravers MT", 27, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label6.Location = System.Drawing.Point(98, 117)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(167, 51)
        self._label6.TabIndex = 11
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(0, 0, 64)
        self._label7.Font = System.Drawing.Font("Engravers MT", 27, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label7.Location = System.Drawing.Point(98, 168)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(167, 45)
        self._label7.TabIndex = 12
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.HotTrack
        self.ClientSize = System.Drawing.Size(606, 267)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog58b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._label6.Text = " "
        self._label7.Text = " "
        self._textBox1.Text = " "
        self._textBox2.Text = " "
        self._textBox3.Text = " "

    def Button3Click(self, sender, e):
        numA = int(self._textBox1.Text)
        numB = int(self._textBox2.Text)
        numC = int(self._textBox3.Text)
        Rootpos = (-numB + math.sqrt(numB**2 - 4*numA*numC))/2*numA
        Rootneg = (-numB - math.sqrt(numB**2 - 4*numA*numC))/2*numA
        self._label6.Text = str(Rootpos)
        self._label7.Text = str(Rootneg)