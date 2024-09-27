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
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label9 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Location = System.Drawing.Point(-13, 198)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(115, 23)
        self._label1.TabIndex = 0
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Location = System.Drawing.Point(343, 126)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(112, 55)
        self._label2.TabIndex = 1
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.White
        self._label3.Location = System.Drawing.Point(172, 235)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(190, 16)
        self._label3.TabIndex = 2
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Location = System.Drawing.Point(183, 225)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(100, 23)
        self._label4.TabIndex = 3
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.White
        self._label5.Location = System.Drawing.Point(251, 212)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(100, 36)
        self._label5.TabIndex = 4
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.White
        self._label6.Location = System.Drawing.Point(-13, 192)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(100, 23)
        self._label6.TabIndex = 5
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.White
        self._label7.Location = System.Drawing.Point(315, 141)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(100, 40)
        self._label7.TabIndex = 6
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.Gold
        self._label8.Location = System.Drawing.Point(315, 9)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(47, 47)
        self._label8.TabIndex = 7
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.PowderBlue
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.White
        self._button1.Location = System.Drawing.Point(202, 256)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(75, 25)
        self._button1.TabIndex = 8
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.PowderBlue
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.White
        self._button2.Location = System.Drawing.Point(283, 256)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(75, 25)
        self._button2.TabIndex = 9
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.PowderBlue
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.White
        self._button3.Location = System.Drawing.Point(364, 256)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(75, 25)
        self._button3.TabIndex = 10
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label9
        # 
        self._label9.Font = System.Drawing.Font("Gadugi", 15.75, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.ForeColor = System.Drawing.Color.PowderBlue
        self._label9.Location = System.Drawing.Point(-3, 7)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(325, 183)
        self._label9.TabIndex = 11
        self._label9.Text = "\"It's not about making money it's about taking money; destroying the status quo because the status is NOT quo. The world is a mess and I just need to rule it.\"            - Dr. Horrible"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.PowderBlue
        self.ClientSize = System.Drawing.Size(451, 282)
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
        self.Controls.Add(self._label9)
        self.Name = "MainForm"
        self.Text = "FavoriteQuote"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label9.ForeColor = System.Drawing.Color.MidnightBlue

    def Button2Click(self, sender, e):
        self._label9.ForeColor = System.Drawing.Color.PowderBlue

    def Button3Click(self, sender, e):
        Application.Exit()