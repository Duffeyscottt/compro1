import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._button5 = System.Windows.Forms.Button()
        self._button6 = System.Windows.Forms.Button()
        self._button7 = System.Windows.Forms.Button()
        self._button8 = System.Windows.Forms.Button()
        self._button9 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.PowderBlue
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.Font = System.Drawing.Font("Segoe Marker", 15, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.FromArgb(192, 64, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(198, 28)
        self._label1.TabIndex = 0
        self._label1.Text = "Number 1:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        self._label1.Click += self.Label1Click
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(110, 14)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(91, 20)
        self._textBox1.TabIndex = 1
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(110, 135)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(91, 20)
        self._textBox2.TabIndex = 3
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.PowderBlue
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label2.Font = System.Drawing.Font("Segoe Marker", 15, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.FromArgb(192, 64, 0)
        self._label2.Location = System.Drawing.Point(12, 130)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(198, 28)
        self._label2.TabIndex = 2
        self._label2.Text = "Number 2:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.DeepSkyBlue
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label3.Font = System.Drawing.Font("Segoe Marker", 15, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.Black
        self._label3.Location = System.Drawing.Point(12, 69)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(198, 28)
        self._label3.TabIndex = 4
        self._label3.Text = "Opperation:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.DeepSkyBlue
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label4.Font = System.Drawing.Font("Segoe Marker", 15, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.Black
        self._label4.Location = System.Drawing.Point(12, 198)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(198, 28)
        self._label4.TabIndex = 5
        self._label4.Text = "Result:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Salmon
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(269, 199)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(123, 28)
        self._button1.TabIndex = 6
        self._button1.Text = "EXIT"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightCyan
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(269, 165)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(123, 28)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.LightCyan
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(300, 108)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(61, 28)
        self._button3.TabIndex = 8
        self._button3.Text = "MOD"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.BackColor = System.Drawing.Color.LightCyan
        self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(233, 74)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(61, 28)
        self._button4.TabIndex = 9
        self._button4.Text = "^"
        self._button4.UseVisualStyleBackColor = False
        self._button4.Click += self.Button4Click
        # 
        # button5
        # 
        self._button5.BackColor = System.Drawing.Color.LightCyan
        self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button5.Location = System.Drawing.Point(300, 74)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(61, 28)
        self._button5.TabIndex = 10
        self._button5.Text = "/"
        self._button5.UseVisualStyleBackColor = False
        self._button5.Click += self.Button5Click
        # 
        # button6
        # 
        self._button6.BackColor = System.Drawing.Color.LightCyan
        self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button6.Location = System.Drawing.Point(367, 74)
        self._button6.Name = "button6"
        self._button6.Size = System.Drawing.Size(61, 28)
        self._button6.TabIndex = 11
        self._button6.Text = "//"
        self._button6.UseVisualStyleBackColor = False
        self._button6.Click += self.Button6Click
        # 
        # button7
        # 
        self._button7.BackColor = System.Drawing.Color.LightCyan
        self._button7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button7.Location = System.Drawing.Point(233, 40)
        self._button7.Name = "button7"
        self._button7.Size = System.Drawing.Size(61, 28)
        self._button7.TabIndex = 12
        self._button7.Text = "+"
        self._button7.UseVisualStyleBackColor = False
        self._button7.Click += self.Button7Click
        # 
        # button8
        # 
        self._button8.BackColor = System.Drawing.Color.LightCyan
        self._button8.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button8.Location = System.Drawing.Point(300, 40)
        self._button8.Name = "button8"
        self._button8.Size = System.Drawing.Size(61, 28)
        self._button8.TabIndex = 13
        self._button8.Text = "-"
        self._button8.UseVisualStyleBackColor = False
        self._button8.Click += self.Button8Click
        # 
        # button9
        # 
        self._button9.BackColor = System.Drawing.Color.LightCyan
        self._button9.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button9.Location = System.Drawing.Point(367, 40)
        self._button9.Name = "button9"
        self._button9.Size = System.Drawing.Size(61, 28)
        self._button9.TabIndex = 14
        self._button9.Text = "*"
        self._button9.UseVisualStyleBackColor = False
        self._button9.Click += self.Button9Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.MediumAquamarine
        self.ClientSize = System.Drawing.Size(446, 261)
        self.Controls.Add(self._button9)
        self.Controls.Add(self._button8)
        self.Controls.Add(self._button7)
        self.Controls.Add(self._button6)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "pg140SimpleCalc"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label1Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._label3.Text = "Opperation:"
        self._label4.Text = "Result:"
        self._textBox1.Text = " "
        self._textBox2.Text = " "

    def Button7Click(self, sender, e):
        self._label3.Text = "Opperation: +"
        num1 = float(self._textBox1.Text)
        num2 = float(self._textBox2.Text)
        result = num1 + num2
        self._label4.Text = "Result: " + str(result)

    def Button8Click(self, sender, e):
        self._label3.Text = "Opperation: -"
        num1 = float(self._textBox1.Text)
        num2 = float(self._textBox2.Text)
        result = num1 - num2
        self._label4.Text = "Result: " + str(result)

    def Button9Click(self, sender, e):
        self._label3.Text = "Opperation: *"
        num1 = float(self._textBox1.Text)
        num2 = float(self._textBox2.Text)
        result = num1 * num2
        self._label4.Text = "Result: " + str(result)

    def Button4Click(self, sender, e):
        self._label3.Text = "Opperation: ^"
        num1 = float(self._textBox1.Text)
        num2 = float(self._textBox2.Text)
        result = num1 ** num2
        self._label4.Text = "Result: " + str(result)

    def Button5Click(self, sender, e):
        self._label3.Text = "Opperation: /"
        num1 = float(self._textBox1.Text)
        num2 = float(self._textBox2.Text)
        result = num1 / num2
        self._label4.Text = "Result: " + str(result)

    def Button6Click(self, sender, e):
        self._label3.Text = "Opperation: //"
        num1 = float(self._textBox1.Text)
        num2 = float(self._textBox2.Text)
        result = num1 // num2
        self._label4.Text = "Result: " + str(result)

    def Button3Click(self, sender, e):
        self._label3.Text = "Opperation: MOD"
        num1 = float(self._textBox1.Text)
        num2 = float(self._textBox2.Text)
        result = num1 % num2
        self._label4.Text = "Result: " + str(result)