import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
        self.dis4n6 = 0.05
        self.dis7n9 = 0.08
        self.dis10more = 0.1
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._groupBox3 = System.Windows.Forms.GroupBox()
        self._groupBox4 = System.Windows.Forms.GroupBox()
        self._calc = System.Windows.Forms.Button()
        self._exit = System.Windows.Forms.Button()
        self._clear = System.Windows.Forms.Button()
        self._yoga = System.Windows.Forms.CheckBox()
        self._karate = System.Windows.Forms.CheckBox()
        self._trainer = System.Windows.Forms.CheckBox()
        self._adult = System.Windows.Forms.RadioButton()
        self._child = System.Windows.Forms.RadioButton()
        self._student = System.Windows.Forms.RadioButton()
        self._senior = System.Windows.Forms.RadioButton()
        self._label1 = System.Windows.Forms.Label()
        self._months = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._fee = System.Windows.Forms.Label()
        self._total = System.Windows.Forms.Label()
        self._groupBox1.SuspendLayout()
        self._groupBox2.SuspendLayout()
        self._groupBox3.SuspendLayout()
        self._groupBox4.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.Color.OrangeRed
        self._groupBox1.Controls.Add(self._senior)
        self._groupBox1.Controls.Add(self._student)
        self._groupBox1.Controls.Add(self._child)
        self._groupBox1.Controls.Add(self._adult)
        self._groupBox1.Font = System.Drawing.Font("Consolas", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.ForeColor = System.Drawing.Color.White
        self._groupBox1.Location = System.Drawing.Point(12, 12)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._groupBox1.Size = System.Drawing.Size(260, 138)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Type of Membership"
        # 
        # groupBox2
        # 
        self._groupBox2.BackColor = System.Drawing.Color.OrangeRed
        self._groupBox2.Controls.Add(self._trainer)
        self._groupBox2.Controls.Add(self._karate)
        self._groupBox2.Controls.Add(self._yoga)
        self._groupBox2.Font = System.Drawing.Font("Consolas", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox2.ForeColor = System.Drawing.Color.White
        self._groupBox2.Location = System.Drawing.Point(278, 12)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._groupBox2.Size = System.Drawing.Size(260, 138)
        self._groupBox2.TabIndex = 1
        self._groupBox2.TabStop = False
        self._groupBox2.Text = "Options"
        # 
        # groupBox3
        # 
        self._groupBox3.BackColor = System.Drawing.Color.OrangeRed
        self._groupBox3.Controls.Add(self._months)
        self._groupBox3.Controls.Add(self._label1)
        self._groupBox3.Font = System.Drawing.Font("Consolas", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox3.ForeColor = System.Drawing.Color.White
        self._groupBox3.Location = System.Drawing.Point(12, 156)
        self._groupBox3.Name = "groupBox3"
        self._groupBox3.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._groupBox3.Size = System.Drawing.Size(260, 138)
        self._groupBox3.TabIndex = 1
        self._groupBox3.TabStop = False
        self._groupBox3.Text = "Membership Length"
        # 
        # groupBox4
        # 
        self._groupBox4.BackColor = System.Drawing.Color.OrangeRed
        self._groupBox4.Controls.Add(self._total)
        self._groupBox4.Controls.Add(self._fee)
        self._groupBox4.Controls.Add(self._label3)
        self._groupBox4.Controls.Add(self._label2)
        self._groupBox4.Font = System.Drawing.Font("Consolas", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox4.ForeColor = System.Drawing.Color.White
        self._groupBox4.Location = System.Drawing.Point(278, 156)
        self._groupBox4.Name = "groupBox4"
        self._groupBox4.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._groupBox4.Size = System.Drawing.Size(260, 138)
        self._groupBox4.TabIndex = 1
        self._groupBox4.TabStop = False
        self._groupBox4.Text = "Membership Fees"
        # 
        # calc
        # 
        self._calc.Font = System.Drawing.Font("Consolas", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._calc.Location = System.Drawing.Point(12, 301)
        self._calc.Name = "calc"
        self._calc.Size = System.Drawing.Size(159, 36)
        self._calc.TabIndex = 2
        self._calc.Text = "Calculate"
        self._calc.UseVisualStyleBackColor = True
        self._calc.Click += self.CalcClick
        # 
        # exit
        # 
        self._exit.Font = System.Drawing.Font("Consolas", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._exit.Location = System.Drawing.Point(379, 301)
        self._exit.Name = "exit"
        self._exit.Size = System.Drawing.Size(159, 36)
        self._exit.TabIndex = 3
        self._exit.Text = "Exit"
        self._exit.UseVisualStyleBackColor = True
        self._exit.Click += self.ExitClick
        # 
        # clear
        # 
        self._clear.Font = System.Drawing.Font("Consolas", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._clear.Location = System.Drawing.Point(196, 301)
        self._clear.Name = "clear"
        self._clear.Size = System.Drawing.Size(159, 36)
        self._clear.TabIndex = 4
        self._clear.Text = "Clear"
        self._clear.UseVisualStyleBackColor = True
        self._clear.Click += self.ClearClick
        # 
        # yoga
        # 
        self._yoga.Location = System.Drawing.Point(33, 35)
        self._yoga.Name = "yoga"
        self._yoga.Size = System.Drawing.Size(104, 24)
        self._yoga.TabIndex = 0
        self._yoga.Text = "Yoga"
        self._yoga.UseVisualStyleBackColor = True
        # 
        # karate
        # 
        self._karate.Location = System.Drawing.Point(33, 65)
        self._karate.Name = "karate"
        self._karate.Size = System.Drawing.Size(104, 24)
        self._karate.TabIndex = 1
        self._karate.Text = "Karate"
        self._karate.UseVisualStyleBackColor = True
        # 
        # trainer
        # 
        self._trainer.Location = System.Drawing.Point(33, 95)
        self._trainer.Name = "trainer"
        self._trainer.Size = System.Drawing.Size(177, 24)
        self._trainer.TabIndex = 2
        self._trainer.Text = "Personal Trainer"
        self._trainer.UseVisualStyleBackColor = True
        # 
        # adult
        # 
        self._adult.Location = System.Drawing.Point(25, 19)
        self._adult.Name = "adult"
        self._adult.Size = System.Drawing.Size(168, 24)
        self._adult.TabIndex = 0
        self._adult.TabStop = True
        self._adult.Text = "Standard Adult"
        self._adult.UseVisualStyleBackColor = True
        # 
        # child
        # 
        self._child.Location = System.Drawing.Point(25, 49)
        self._child.Name = "child"
        self._child.Size = System.Drawing.Size(211, 24)
        self._child.TabIndex = 1
        self._child.TabStop = True
        self._child.Text = "Child (12 and under)"
        self._child.UseVisualStyleBackColor = True
        # 
        # student
        # 
        self._student.Location = System.Drawing.Point(25, 79)
        self._student.Name = "student"
        self._student.Size = System.Drawing.Size(168, 24)
        self._student.TabIndex = 2
        self._student.TabStop = True
        self._student.Text = "Student"
        self._student.UseVisualStyleBackColor = True
        # 
        # senior
        # 
        self._senior.Location = System.Drawing.Point(25, 109)
        self._senior.Name = "senior"
        self._senior.Size = System.Drawing.Size(168, 24)
        self._senior.TabIndex = 3
        self._senior.TabStop = True
        self._senior.Text = "Senior Citizen"
        self._senior.UseVisualStyleBackColor = True
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(33, 33)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(168, 45)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter the number of months:"
        # 
        # months
        # 
        self._months.Location = System.Drawing.Point(25, 81)
        self._months.Name = "months"
        self._months.Size = System.Drawing.Size(211, 26)
        self._months.TabIndex = 1
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(6, 33)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(118, 26)
        self._label2.TabIndex = 2
        self._label2.Text = "Monthly Fee:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(6, 77)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(118, 26)
        self._label3.TabIndex = 3
        self._label3.Text = "Total:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # fee
        # 
        self._fee.BackColor = System.Drawing.Color.Snow
        self._fee.ForeColor = System.Drawing.Color.Black
        self._fee.Location = System.Drawing.Point(130, 37)
        self._fee.Name = "fee"
        self._fee.Size = System.Drawing.Size(113, 26)
        self._fee.TabIndex = 4
        # 
        # total
        # 
        self._total.BackColor = System.Drawing.Color.Snow
        self._total.ForeColor = System.Drawing.Color.Black
        self._total.Location = System.Drawing.Point(130, 81)
        self._total.Name = "total"
        self._total.Size = System.Drawing.Size(113, 26)
        self._total.TabIndex = 5
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.OrangeRed
        self.ClientSize = System.Drawing.Size(551, 349)
        self.Controls.Add(self._clear)
        self.Controls.Add(self._exit)
        self.Controls.Add(self._calc)
        self.Controls.Add(self._groupBox4)
        self.Controls.Add(self._groupBox3)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._groupBox1)
        self.Name = "MainForm"
        self.Text = "Pg250MembershipFee"
        self._groupBox1.ResumeLayout(False)
        self._groupBox2.ResumeLayout(False)
        self._groupBox3.ResumeLayout(False)
        self._groupBox3.PerformLayout()
        self._groupBox4.ResumeLayout(False)
        self.ResumeLayout(False)


    def ExitClick(self, sender, e):
        Application.Exit()

    def ClearClick(self, sender, e):
        self._adult.Checked = True
        self._yoga.Checked = False
        self._karate.Checked = False
        self._trainer.Checked = False
        self._months.Clear()
        self._fee.Text = ""
        self._total.Text = ""

    def CalcClick(self, sender, e):
        base = 0.0
        discount = 0.0
        totalfee = 0.0
        months = 0.0
        
        try:
            months = int(self._months.Text)
        except:
            MessageBox.Show("Months must be a valid integer", "Input Error")
        
        if months < 1 or months > 24:
            MessageBox.Show("Months must be a valid integer", "Input Error")
            
        if self._adult.Checked == True:
            base = 40
        elif self._child.Checked == True:
            base = 20
        elif self._student.Checked == True:
            base = 25
        elif self._senior.Checked == True:
            base = 30
            
        if self._yoga.Checked == True:
            base += 10
        if self._karate.Checked == True:
            base += 30
        if self._trainer.Checked == True:
            base += 50
            
        if months <= 3:
            discount = 0.0
        elif months >= 4 and months <= 6:
            discount = self.dis4n6 * base
        elif months >= 7 and months <= 9:
            discount = self.dis7n9 * base
        elif months >= 10:
            discount = self.dis10more * base
            
        base -= discount
        totalfee = base * months
        
        self._fee.Text = "$" + str(round(base, 2))
        self._total.Text = "$" + str(round(totalfee, 2))