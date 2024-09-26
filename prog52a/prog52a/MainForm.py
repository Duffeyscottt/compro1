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
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.MediumAquamarine
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.FromArgb(0, 0, 64)
        self._label1.Location = System.Drawing.Point(12, 30)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 30)
        self._label1.TabIndex = 0
        self._label1.Text = "length:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.MediumAquamarine
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.FromArgb(0, 0, 64)
        self._label2.Location = System.Drawing.Point(12, 69)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 30)
        self._label2.TabIndex = 1
        self._label2.Text = "width:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.MediumTurquoise
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.FromArgb(0, 0, 64)
        self._label3.Location = System.Drawing.Point(13, 162)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(99, 34)
        self._label3.TabIndex = 2
        self._label3.Text = "area:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.MediumTurquoise
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.FromArgb(0, 0, 64)
        self._label4.Location = System.Drawing.Point(13, 210)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(99, 34)
        self._label4.TabIndex = 3
        self._label4.Text = "perimeter:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label4.Click += self.Label4Click
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.MediumTurquoise
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.Color.FromArgb(0, 0, 64)
        self._label5.Location = System.Drawing.Point(118, 162)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(213, 34)
        self._label5.TabIndex = 4
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.MediumTurquoise
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.Color.FromArgb(0, 0, 64)
        self._label6.Location = System.Drawing.Point(118, 210)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(213, 34)
        self._label6.TabIndex = 5
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Cyan
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.FromArgb(0, 0, 64)
        self._button1.Location = System.Drawing.Point(360, 83)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(100, 49)
        self._button1.TabIndex = 6
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Cyan
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.FromArgb(0, 0, 64)
        self._button2.Location = System.Drawing.Point(360, 150)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(100, 49)
        self._button2.TabIndex = 7
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Cyan
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.FromArgb(0, 0, 64)
        self._button3.Location = System.Drawing.Point(360, 221)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(100, 49)
        self._button3.TabIndex = 8
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.ForeColor = System.Drawing.Color.FromArgb(0, 0, 64)
        self._textBox1.Location = System.Drawing.Point(118, 30)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(213, 30)
        self._textBox1.TabIndex = 9
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.ForeColor = System.Drawing.Color.FromArgb(0, 0, 64)
        self._textBox2.Location = System.Drawing.Point(118, 69)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(213, 30)
        self._textBox2.TabIndex = 10
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(0, 0, 64)
        self.ClientSize = System.Drawing.Size(472, 282)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog52a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label4Click(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        self._textBox1.Text = " "
        self._textBox2.Text = " "
        self._label5.Text = " "
        self._label6.Text = " "

    def Button1Click(self, sender, e):
        length = int(self._textBox1.Text)
        width = int(self._textBox2.Text)
        area = length * width
        perimeter = 2 * length + 2 * width
        self._label5.Text = str(area)
        self._label6.Text = str(perimeter)
        # + - * / %     ** pow    // divide & round down
        # int (Integer): a whole number, pos/neg
        # float (floating point number): any number w/ decimal
        # str (string): a string of text
        
        

    def Button3Click(self, sender, e):
        Application.Exit()