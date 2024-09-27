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
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self._button3 = System.Windows.Forms.Button()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Ivory
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Gray
        self._label1.Location = System.Drawing.Point(16, 45)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(263, 216)
        self._label1.TabIndex = 1
        self._label1.Text = "This area is empty. "
        self._label1.Click += self.Label1Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.DarkOrange
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.SaddleBrown
        self._label2.Location = System.Drawing.Point(385, 27)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(202, 53)
        self._label2.TabIndex = 1
        self._label2.Text = "clear"
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.White
        self._button1.ForeColor = System.Drawing.Color.Gray
        self._button1.Location = System.Drawing.Point(389, 53)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(193, 23)
        self._button1.TabIndex = 2
        self._button1.Text = "click here to clear"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.White
        self._button2.ForeColor = System.Drawing.Color.Gray
        self._button2.Location = System.Drawing.Point(310, 208)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(108, 41)
        self._button2.TabIndex = 2
        self._button2.Text = "click here to show"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.DeepSkyBlue
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.HotTrack
        self._label3.Location = System.Drawing.Point(306, 182)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(117, 71)
        self._label3.TabIndex = 3
        self._label3.Text = "show"
        self._label3.Click += self.Label3Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.White
        self._button3.ForeColor = System.Drawing.Color.Gray
        self._button3.Location = System.Drawing.Point(622, 243)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(98, 71)
        self._button3.TabIndex = 6
        self._button3.Text = "click here to exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Red
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.FromArgb(64, 0, 0)
        self._label4.Location = System.Drawing.Point(618, 217)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(107, 101)
        self._label4.TabIndex = 5
        self._label4.Text = "exit"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label5.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.Color.DarkGreen
        self._label5.Location = System.Drawing.Point(12, 13)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(273, 253)
        self._label5.TabIndex = 7
        self._label5.Text = "about me"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(0, 0, 64)
        self.ClientSize = System.Drawing.Size(737, 327)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._label5)
        self.ForeColor = System.Drawing.SystemColors.AppWorkspace
        self.Name = "MainForm"
        self.Text = "About Me"
        self.ResumeLayout(False)


    def TextBox1TextChanged(self, sender, e):
        pass

    def Label2Click(self, sender, e):
        pass

    def Label3Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        self._label1.Text = "This area is empty."
        self._label1.ForeColor = Color.Gray
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)

    def Button3Click(self, sender, e):
        Application.Exit()

    def Label1Click(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        self._label1.Text = "My last name has an uncomon spelling of Duffey instead of Duffy or Duffie and my dad thinks it's because one of our ancestors was some illiterate scottish farmer that just guessed the spelling." #placeholder text
        self._label1.ForeColor = Color.Black
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)