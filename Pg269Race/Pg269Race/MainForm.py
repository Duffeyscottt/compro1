import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._run1 = System.Windows.Forms.TextBox()
        self._run2 = System.Windows.Forms.TextBox()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._sec3 = System.Windows.Forms.TextBox()
        self._sec2 = System.Windows.Forms.TextBox()
        self._sec1 = System.Windows.Forms.TextBox()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._third = System.Windows.Forms.Label()
        self._first = System.Windows.Forms.Label()
        self._second = System.Windows.Forms.Label()
        self._groupBox1.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.Controls.Add(self._third)
        self._groupBox1.Controls.Add(self._first)
        self._groupBox1.Controls.Add(self._second)
        self._groupBox1.Controls.Add(self._label7)
        self._groupBox1.Controls.Add(self._label9)
        self._groupBox1.Controls.Add(self._label8)
        self._groupBox1.Location = System.Drawing.Point(12, 217)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(353, 135)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Race Results"
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.PeachPuff
        self._button1.ForeColor = System.Drawing.Color.SaddleBrown
        self._button1.Location = System.Drawing.Point(41, 380)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(93, 39)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate Results"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.PeachPuff
        self._button2.ForeColor = System.Drawing.Color.SaddleBrown
        self._button2.Location = System.Drawing.Point(140, 380)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(93, 39)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.PeachPuff
        self._button3.ForeColor = System.Drawing.Color.SaddleBrown
        self._button3.Location = System.Drawing.Point(239, 380)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(93, 39)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 17, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(353, 69)
        self._label1.TabIndex = 4
        self._label1.Text = "Enter the three runners' names and finishing times"
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(101, 89)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(45, 23)
        self._label2.TabIndex = 5
        self._label2.Text = "Name"
        self._label2.TextAlign = System.Drawing.ContentAlignment.BottomLeft
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(239, 77)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(70, 35)
        self._label3.TabIndex = 6
        self._label3.Text = "Seconds to Finish"
        self._label3.TextAlign = System.Drawing.ContentAlignment.BottomLeft
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 115)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(74, 30)
        self._label4.TabIndex = 7
        self._label4.Text = "Runner 1:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.TopRight
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(12, 145)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(74, 30)
        self._label5.TabIndex = 8
        self._label5.Text = "Runner 2:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.TopRight
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(12, 175)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(74, 30)
        self._label6.TabIndex = 9
        self._label6.Text = "Runner 3:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.TopRight
        # 
        # run1
        # 
        self._run1.Location = System.Drawing.Point(92, 115)
        self._run1.Multiline = True
        self._run1.Name = "run1"
        self._run1.Size = System.Drawing.Size(93, 22)
        self._run1.TabIndex = 10
        self._run1.TextChanged += self.TextBox1TextChanged
        # 
        # run2
        # 
        self._run2.Location = System.Drawing.Point(92, 145)
        self._run2.Multiline = True
        self._run2.Name = "run2"
        self._run2.Size = System.Drawing.Size(93, 22)
        self._run2.TabIndex = 11
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(92, 175)
        self._textBox1.Multiline = True
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(93, 22)
        self._textBox1.TabIndex = 12
        # 
        # sec3
        # 
        self._sec3.Location = System.Drawing.Point(239, 175)
        self._sec3.Multiline = True
        self._sec3.Name = "sec3"
        self._sec3.Size = System.Drawing.Size(70, 22)
        self._sec3.TabIndex = 15
        # 
        # sec2
        # 
        self._sec2.Location = System.Drawing.Point(239, 145)
        self._sec2.Multiline = True
        self._sec2.Name = "sec2"
        self._sec2.Size = System.Drawing.Size(70, 22)
        self._sec2.TabIndex = 14
        # 
        # sec1
        # 
        self._sec1.Location = System.Drawing.Point(239, 115)
        self._sec1.Multiline = True
        self._sec1.Name = "sec1"
        self._sec1.Size = System.Drawing.Size(70, 22)
        self._sec1.TabIndex = 13
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(67, 90)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(105, 30)
        self._label7.TabIndex = 18
        self._label7.Text = "Third Place:"
        self._label7.TextAlign = System.Drawing.ContentAlignment.TopRight
        # 
        # label8
        # 
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(67, 60)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(105, 30)
        self._label8.TabIndex = 17
        self._label8.Text = "Second Place:"
        self._label8.TextAlign = System.Drawing.ContentAlignment.TopRight
        # 
        # label9
        # 
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(67, 30)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(105, 30)
        self._label9.TabIndex = 16
        self._label9.Text = "First Place:"
        self._label9.TextAlign = System.Drawing.ContentAlignment.TopRight
        # 
        # third
        # 
        self._third.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._third.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._third.Location = System.Drawing.Point(178, 90)
        self._third.Name = "third"
        self._third.Size = System.Drawing.Size(74, 22)
        self._third.TabIndex = 21
        self._third.TextAlign = System.Drawing.ContentAlignment.TopRight
        # 
        # first
        # 
        self._first.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._first.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._first.Location = System.Drawing.Point(178, 30)
        self._first.Name = "first"
        self._first.Size = System.Drawing.Size(74, 22)
        self._first.TabIndex = 19
        self._first.TextAlign = System.Drawing.ContentAlignment.TopRight
        # 
        # second
        # 
        self._second.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._second.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._second.Location = System.Drawing.Point(178, 60)
        self._second.Name = "second"
        self._second.Size = System.Drawing.Size(74, 22)
        self._second.TabIndex = 20
        self._second.TextAlign = System.Drawing.ContentAlignment.TopRight
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.SeaShell
        self.ClientSize = System.Drawing.Size(377, 431)
        self.Controls.Add(self._sec3)
        self.Controls.Add(self._sec2)
        self.Controls.Add(self._sec1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._run2)
        self.Controls.Add(self._run1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._groupBox1)
        self.Name = "MainForm"
        self.Text = "Pg269Race"
        self._groupBox1.ResumeLayout(False)
        self.ResumeLayout(False)
        self.PerformLayout()


    def TextBox1TextChanged(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        run1 = str(self._run1.Text)
        run2 = str(self._run2.Text)
        run3 = str(self._run2.Text)
        sec1 = int(self._sec1.Text)
        sec2 = int(self._sec2.Text)
        sec3 = int(self._sec3.Text)
        
        if sec1 < sec2:
            if sec1 < sec3:
                self._first.Text = str(run1)
                if sec2 < sec3:
                    self._second.Text = str(run2)
                    self._third.Text = str(run3)
                else:
                    self._second.Text = str(run3)
                    self._third.Text = str(run2)
            else:
                self._second.Text = str(run3)
                if sec2 < sec3:
                    self._second.Text = str(run2)
                    self._third.Text = str(run3)
                else:
                    self._second.Text = str(run3)
                    self._third.Text = str(run2)
                
        
        
        
        
        
        
        
        """ wanted to do this but didn't know how to connect to names
        times = [sec1, sec2, sec3]
        times.sort()"""
        
        
        
        