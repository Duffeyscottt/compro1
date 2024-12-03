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
        self._choice1 = System.Windows.Forms.RadioButton()
        self._choice2 = System.Windows.Forms.RadioButton()
        self._choice3 = System.Windows.Forms.RadioButton()
        self._choice4 = System.Windows.Forms.CheckBox()
        self._choice5 = System.Windows.Forms.CheckBox()
        self._choice6 = System.Windows.Forms.CheckBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._groupBox1.SuspendLayout()
        self._groupBox2.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.Controls.Add(self._choice3)
        self._groupBox1.Controls.Add(self._choice2)
        self._groupBox1.Controls.Add(self._choice1)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.ForeColor = System.Drawing.Color.White
        self._groupBox1.Location = System.Drawing.Point(12, 24)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(250, 234)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Radio Buttons"
        # 
        # groupBox2
        # 
        self._groupBox2.Controls.Add(self._choice6)
        self._groupBox2.Controls.Add(self._choice5)
        self._groupBox2.Controls.Add(self._choice4)
        self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox2.ForeColor = System.Drawing.Color.White
        self._groupBox2.Location = System.Drawing.Point(274, 24)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.RightToLeft = System.Windows.Forms.RightToLeft.Yes
        self._groupBox2.Size = System.Drawing.Size(250, 234)
        self._groupBox2.TabIndex = 1
        self._groupBox2.TabStop = False
        self._groupBox2.Text = "Check Boxes"
        # 
        # choice1
        # 
        self._choice1.Font = System.Drawing.Font("Microsoft Sans Serif", 17, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._choice1.Location = System.Drawing.Point(17, 49)
        self._choice1.Name = "choice1"
        self._choice1.Size = System.Drawing.Size(182, 31)
        self._choice1.TabIndex = 0
        self._choice1.TabStop = True
        self._choice1.Text = "Choice 1"
        self._choice1.UseVisualStyleBackColor = True
        # 
        # choice2
        # 
        self._choice2.Font = System.Drawing.Font("Microsoft Sans Serif", 17, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._choice2.Location = System.Drawing.Point(17, 104)
        self._choice2.Name = "choice2"
        self._choice2.Size = System.Drawing.Size(182, 31)
        self._choice2.TabIndex = 1
        self._choice2.TabStop = True
        self._choice2.Text = "Choice 2"
        self._choice2.UseVisualStyleBackColor = True
        # 
        # choice3
        # 
        self._choice3.Font = System.Drawing.Font("Microsoft Sans Serif", 17, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._choice3.Location = System.Drawing.Point(17, 162)
        self._choice3.Name = "choice3"
        self._choice3.Size = System.Drawing.Size(182, 31)
        self._choice3.TabIndex = 2
        self._choice3.TabStop = True
        self._choice3.Text = "Choice 3"
        self._choice3.UseVisualStyleBackColor = True
        # 
        # choice4
        # 
        self._choice4.Font = System.Drawing.Font("Microsoft Sans Serif", 17, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._choice4.Location = System.Drawing.Point(75, 43)
        self._choice4.Name = "choice4"
        self._choice4.Size = System.Drawing.Size(155, 44)
        self._choice4.TabIndex = 0
        self._choice4.Text = "Choice 4"
        self._choice4.UseVisualStyleBackColor = True
        # 
        # choice5
        # 
        self._choice5.Font = System.Drawing.Font("Microsoft Sans Serif", 17, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._choice5.Location = System.Drawing.Point(75, 98)
        self._choice5.Name = "choice5"
        self._choice5.Size = System.Drawing.Size(155, 44)
        self._choice5.TabIndex = 1
        self._choice5.Text = "Choice 5"
        self._choice5.UseVisualStyleBackColor = True
        # 
        # choice6
        # 
        self._choice6.Font = System.Drawing.Font("Microsoft Sans Serif", 17, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._choice6.Location = System.Drawing.Point(75, 156)
        self._choice6.Name = "choice6"
        self._choice6.Size = System.Drawing.Size(155, 44)
        self._choice6.TabIndex = 2
        self._choice6.Text = "Choice 6"
        self._choice6.UseVisualStyleBackColor = True
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(94, 264)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(138, 33)
        self._button1.TabIndex = 2
        self._button1.Text = "ok"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(308, 264)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(138, 33)
        self._button2.TabIndex = 3
        self._button2.Text = "exit"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(536, 309)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._groupBox1)
        self.Name = "MainForm"
        self.Text = "Pg247Radio"
        self._groupBox1.ResumeLayout(False)
        self._groupBox2.ResumeLayout(False)
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        strMessage = ""
        
        if self._choice1.Checked == True:
            strMessage = "You have selected Choice 1"
        elif self._choice2.Checked == True:
            strMessage = "You have selected Choice 2"
        elif self._choice3.Checked == True:
            strMessage = "You have selected Choice 3"
            
        if self._choice4.Checked == True:
            strMessage += " and Choice 4"
        if self._choice5.Checked == True:
            strMessage += " and Choice 5"
        if self._choice6.Checked == True:
            strMessage += " and Choice 6"
            
        MessageBox.Show(strMessage)

    def Button2Click(self, sender, e):
        Application.Exit()