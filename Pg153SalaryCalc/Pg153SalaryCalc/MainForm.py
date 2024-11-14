import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._button3 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(149, 18)
        self._textBox1.Multiline = True
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(123, 24)
        self._textBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Crimson
        self._button1.Location = System.Drawing.Point(12, 179)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(123, 28)
        self._button1.TabIndex = 3
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Haettenschweiler", 22, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.Crimson
        self._label2.Location = System.Drawing.Point(3, 9)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(148, 40)
        self._label2.TabIndex = 4
        self._label2.Text = "Annual Salary:"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Haettenschweiler", 22, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.Crimson
        self._label3.Location = System.Drawing.Point(3, 64)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(148, 40)
        self._label3.TabIndex = 6
        self._label3.Text = "Pay Periods:"
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(149, 73)
        self._textBox2.Multiline = True
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(123, 24)
        self._textBox2.TabIndex = 5
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Haettenschweiler", 14.2, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Crimson
        self._label1.Location = System.Drawing.Point(3, 134)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(148, 40)
        self._label1.TabIndex = 7
        self._label1.Text = "Salary Per Pay Period:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.MistyRose
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label4.Font = System.Drawing.Font("Haettenschweiler", 14.2, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.Crimson
        self._label4.Location = System.Drawing.Point(149, 134)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(123, 28)
        self._label4.TabIndex = 8
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Crimson
        self._button3.Location = System.Drawing.Point(149, 179)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(123, 28)
        self._button3.TabIndex = 10
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Black
        self._button2.Location = System.Drawing.Point(81, 213)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(123, 36)
        self._button2.TabIndex = 11
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Pink
        self.ClientSize = System.Drawing.Size(284, 261)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button2)
        self.Name = "MainForm"
        self.Text = "Pg153SalaryCalc"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        try:
            salary = float(self._textBox1.Text)
            period   = int(self._textBox2.Text)
        except:
            MessageBox.Show("The input files must contain nonzero numeric values.", "Error")
        
        salaryper = salary / period
        self._label4.Text = "$ " + str(round(salaryper, 2))
        

    def Button3Click(self, sender, e):
        self._textBox1.Text = " "
        self._textBox2.Text = " "
        self._label4.Text = " "

    def Button2Click(self, sender, e):
        Application.Exit()