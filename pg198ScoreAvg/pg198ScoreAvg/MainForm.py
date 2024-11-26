import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._groupBox1.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.Controls.Add(self._label5)
        self._groupBox1.Controls.Add(self._label4)
        self._groupBox1.Controls.Add(self._textBox3)
        self._groupBox1.Controls.Add(self._label3)
        self._groupBox1.Controls.Add(self._textBox2)
        self._groupBox1.Controls.Add(self._label2)
        self._groupBox1.Controls.Add(self._textBox1)
        self._groupBox1.Controls.Add(self._label1)
        self._groupBox1.Font = System.Drawing.Font("Bradley Hand ITC", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.ForeColor = System.Drawing.SystemColors.Highlight
        self._groupBox1.Location = System.Drawing.Point(12, 12)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(312, 203)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Enter Three Test Scores"
        self._groupBox1.Enter += self.GroupBox1Enter
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Bradley Hand ITC", 14, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Red
        self._label1.Location = System.Drawing.Point(22, 33)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(90, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "Score 1:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.BottomRight
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.SystemColors.Info
        self._textBox1.Font = System.Drawing.Font("Bradley Hand ITC", 11, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(109, 33)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(131, 26)
        self._textBox1.TabIndex = 1
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.SystemColors.Info
        self._textBox2.Font = System.Drawing.Font("Bradley Hand ITC", 11, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(109, 75)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(131, 26)
        self._textBox2.TabIndex = 3
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Bradley Hand ITC", 14, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.Red
        self._label2.Location = System.Drawing.Point(22, 75)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(90, 23)
        self._label2.TabIndex = 2
        self._label2.Text = "Score 2:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.BottomRight
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.SystemColors.Info
        self._textBox3.Font = System.Drawing.Font("Bradley Hand ITC", 11, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(109, 117)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(131, 26)
        self._textBox3.TabIndex = 5
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Bradley Hand ITC", 14, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.Red
        self._label3.Location = System.Drawing.Point(22, 117)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(90, 23)
        self._label3.TabIndex = 4
        self._label3.Text = "Score 3:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.BottomRight
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Bradley Hand ITC", 17, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.Highlight
        self._label4.Location = System.Drawing.Point(6, 146)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(106, 49)
        self._label4.TabIndex = 6
        self._label4.Text = "Average:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.BottomRight
        # 
        # label5
        # 
        self._label5.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label5.Font = System.Drawing.Font("Buxton Sketch", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.SystemColors.InfoText
        self._label5.Location = System.Drawing.Point(109, 165)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(131, 30)
        self._label5.TabIndex = 7
        self._label5.TextAlign = System.Drawing.ContentAlignment.BottomLeft
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.Info
        self._button1.Font = System.Drawing.Font("Bradley Hand ITC", 14, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.Highlight
        self._button1.Location = System.Drawing.Point(34, 250)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(104, 67)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate Average"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.Info
        self._button2.Font = System.Drawing.Font("Bradley Hand ITC", 14, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.Highlight
        self._button2.Location = System.Drawing.Point(184, 250)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(104, 29)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.Info
        self._button3.Font = System.Drawing.Font("Bradley Hand ITC", 14, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Red
        self._button3.Location = System.Drawing.Point(184, 288)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(104, 29)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.Info
        self.ClientSize = System.Drawing.Size(336, 355)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._groupBox1)
        self.Name = "MainForm"
        self.Text = "pg198ScoreAvg"
        self._groupBox1.ResumeLayout(False)
        self._groupBox1.PerformLayout()
        self.ResumeLayout(False)


    def GroupBox1Enter(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._label5.Text = ""

    def Button1Click(self, sender, e):
        a = float(self._textBox1.Text)
        b = float(self._textBox2.Text)
        c = float(self._textBox3.Text)
        add = a + b + c
        avg = add / 3
        self._label5.Text = str(round(avg, 2))