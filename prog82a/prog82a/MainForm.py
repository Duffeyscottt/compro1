import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 250)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(208, 23)
        self._button1.TabIndex = 0
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(442, 250)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(208, 23)
        self._button2.TabIndex = 1
        self._button2.Text = "exit"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(227, 250)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(208, 23)
        self._button3.TabIndex = 2
        self._button3.Text = "clear"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Orange
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 53)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 3
        self._label1.Text = "Speed Limit:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.Orange
        self._textBox1.Location = System.Drawing.Point(118, 53)
        self._textBox1.Multiline = True
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(129, 23)
        self._textBox1.TabIndex = 4
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Orange
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(369, 53)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 5
        self._label2.Text = "Speed:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.Orange
        self._textBox2.Location = System.Drawing.Point(475, 53)
        self._textBox2.Multiline = True
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(129, 23)
        self._textBox2.TabIndex = 6
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Green
        self._label3.Font = System.Drawing.Font("Playbill", 50, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ImageAlign = System.Drawing.ContentAlignment.BottomLeft
        self._label3.Location = System.Drawing.Point(343, 108)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(244, 117)
        self._label3.TabIndex = 7
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ImageAlign = System.Drawing.ContentAlignment.BottomLeft
        self._label4.Location = System.Drawing.Point(-73, -108)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(360, 131)
        self._label4.TabIndex = 8
        self._label4.Text = "Fine:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Green
        self._label5.Font = System.Drawing.Font("Playbill", 62, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ImageAlign = System.Drawing.ContentAlignment.BottomLeft
        self._label5.Location = System.Drawing.Point(227, 94)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(360, 131)
        self._label5.TabIndex = 9
        self._label5.Text = "Fine:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Black
        self.ClientSize = System.Drawing.Size(662, 285)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label5)
        self.Name = "MainForm"
        self.Text = "prog82a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button2Click(self, sender, e):
        Application.Exit()

    def Button3Click(self, sender, e):
        self._label3.Text = " "
        self._textBox1.Text = " "
        self._textBox2.Text = " "

    def Button1Click(self, sender, e):
        limit = int(self._textBox1.Text)
        speed = int(self._textBox2.Text)
        if speed > limit:
            over = speed - limit
            fine = 20.00 + (over * 5.00)
            self._label3.Text = "$" + str(fine)