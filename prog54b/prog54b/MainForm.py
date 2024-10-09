import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.Pink
        self._textBox1.Font = System.Drawing.Font("Segoe UI Black", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.ForeColor = System.Drawing.Color.HotPink
        self._textBox1.Location = System.Drawing.Point(13, 25)
        self._textBox1.Multiline = True
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(84, 49)
        self._textBox1.TabIndex = 0
        self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # textBox4
        # 
        self._textBox4.BackColor = System.Drawing.Color.Pink
        self._textBox4.Font = System.Drawing.Font("Segoe UI Black", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.ForeColor = System.Drawing.Color.HotPink
        self._textBox4.Location = System.Drawing.Point(103, 25)
        self._textBox4.Multiline = True
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(84, 49)
        self._textBox4.TabIndex = 3
        self._textBox4.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.Pink
        self._textBox3.Font = System.Drawing.Font("Segoe UI Black", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.ForeColor = System.Drawing.Color.HotPink
        self._textBox3.Location = System.Drawing.Point(193, 25)
        self._textBox3.Multiline = True
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(84, 49)
        self._textBox3.TabIndex = 4
        self._textBox3.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.Pink
        self._textBox2.Font = System.Drawing.Font("Segoe UI Black", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.ForeColor = System.Drawing.Color.HotPink
        self._textBox2.Location = System.Drawing.Point(283, 25)
        self._textBox2.Multiline = True
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(84, 49)
        self._textBox2.TabIndex = 5
        self._textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.GhostWhite
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Orchid
        self._button1.Location = System.Drawing.Point(12, 88)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(76, 36)
        self._button1.TabIndex = 6
        self._button1.Text = "Sum"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Plum
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.LavenderBlush
        self._label1.Location = System.Drawing.Point(94, 93)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(183, 25)
        self._label1.TabIndex = 7
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Plum
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.LavenderBlush
        self._label2.Location = System.Drawing.Point(94, 143)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(183, 25)
        self._label2.TabIndex = 9
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.GhostWhite
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 11, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Orchid
        self._button2.Location = System.Drawing.Point(12, 138)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(76, 36)
        self._button2.TabIndex = 8
        self._button2.Text = "Average"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.GhostWhite
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Orchid
        self._button3.Location = System.Drawing.Point(328, 98)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(89, 32)
        self._button3.TabIndex = 10
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.BackColor = System.Drawing.Color.GhostWhite
        self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.ForeColor = System.Drawing.Color.Orchid
        self._button4.Location = System.Drawing.Point(328, 136)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(89, 32)
        self._button4.TabIndex = 11
        self._button4.Text = "Exit"
        self._button4.UseVisualStyleBackColor = False
        self._button4.Click += self.Button4Click
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.LightPink
        self._label3.Location = System.Drawing.Point(13, 12)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(183, 23)
        self._label3.TabIndex = 12
        self._label3.Text = "Put in 3-digit numbers below"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LavenderBlush
        self.ClientSize = System.Drawing.Size(429, 199)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Name = "MainForm"
        self.Text = "prog54b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button4Click(self, sender, e):
        Application.Exit()

    def Button3Click(self, sender, e):
        self._label1.Text = " "
        self._label2.Text = " "
        self._textBox1.Text = " "
        self._textBox2.Text = " "
        self._textBox3.Text = " "
        self._textBox4.Text = " "

    def Button1Click(self, sender, e):
        num1 = int(self._textBox1.Text)
        num2 = int(self._textBox2.Text)
        num3 = int(self._textBox3.Text)
        num4 = int(self._textBox4.Text)
        Sum = num1 + num2 + num3 + num4
        self._label1.Text = str(Sum)

    def Button2Click(self, sender, e):
        num1 = int(self._textBox1.Text)
        num2 = int(self._textBox2.Text)
        num3 = int(self._textBox3.Text)
        num4 = int(self._textBox4.Text)
        Sum = num1 + num2 + num3 + num4
        Average = Sum/4.0
        self._label2.Text = str(Average)