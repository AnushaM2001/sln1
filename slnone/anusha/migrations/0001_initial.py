# Generated by Django 5.0.6 on 2024-08-11 14:28

import anusha.models
import datetime
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllInsurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15, unique=True)),
                ('email_id', models.EmailField(max_length=254)),
                ('messgae', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='basicdetailform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=25, validators=[anusha.models.validate_only_letters])),
                ('pan_number', models.CharField(max_length=10, validators=[anusha.models.validate_pan])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10)),
                ('email', models.EmailField(max_length=254, validators=[anusha.models.validate_email])),
                ('date_of_birth', models.DateField(validators=[anusha.models.validate_date])),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')], default='Single', max_length=10)),
                ('required_loan_amount', models.CharField(max_length=10, validators=[anusha.models.validate_amount])),
                ('terms_accepted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('random_number', models.CharField(blank=True, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralInsurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15, unique=True)),
                ('email_id', models.EmailField(max_length=254)),
                ('messgae', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='goldbasicdetailform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=25, validators=[anusha.models.validate_only_letters])),
                ('pan_number', models.CharField(max_length=10, validators=[anusha.models.validate_pan])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10)),
                ('email', models.EmailField(max_length=254, validators=[anusha.models.validate_email])),
                ('date_of_birth', models.DateField(validators=[anusha.models.validate_date])),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')], default='Single', max_length=10)),
                ('required_loan_amount', models.IntegerField(validators=[anusha.models.validate_amount])),
                ('terms_accepted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('random_number', models.CharField(blank=True, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Goldloanapplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[anusha.models.validate_only_letters])),
                ('email', models.EmailField(blank=True, max_length=254, null=True, validators=[anusha.models.validate_email])),
                ('contact_no', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_contact_number', message='Contact number must be 10 digits.', regex='^\\d{10}$')])),
                ('state', models.CharField(max_length=50, validators=[anusha.models.validate_only_letters])),
                ('pincode', models.CharField(max_length=6, validators=[anusha.models.validate_pincode])),
                ('random_number', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='healthInsurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15, unique=True)),
                ('email_id', models.EmailField(max_length=254)),
                ('messgae', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LifeInsurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15, unique=True)),
                ('email_id', models.EmailField(max_length=254)),
                ('messgae', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LoanApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_type', models.CharField(choices=[('LAP', 'Loan Against Property'), ('LAPBT', 'Loan Against Property with Business Tenure')], max_length=10)),
                ('first_name', models.CharField(max_length=50, validators=[anusha.models.validate_only_letters])),
                ('last_name', models.CharField(max_length=50, validators=[anusha.models.validate_only_letters])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('date_of_birth', models.DateField(validators=[anusha.models.validate_date])),
                ('mobile_number', models.CharField(max_length=10, validators=[anusha.models.validate_mobile_number])),
                ('pan_card_number', models.CharField(max_length=10, validators=[anusha.models.validate_pan])),
                ('aadhar_card_number', models.CharField(max_length=12, validators=[anusha.models.validate_aadhar_number])),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')], max_length=10)),
                ('email_id', models.EmailField(max_length=254, validators=[anusha.models.validate_email])),
                ('current_address', models.TextField(validators=[anusha.models.validate_address])),
                ('current_address_pincode', models.CharField(max_length=6, validators=[anusha.models.validate_pincode])),
                ('aadhar_address', models.TextField(validators=[anusha.models.validate_address])),
                ('aadhar_pincode', models.CharField(max_length=6, validators=[anusha.models.validate_pincode])),
                ('income_source', models.CharField(choices=[('JOB', 'Job'), ('BUSINESS', 'Business')], max_length=10)),
                ('net_salary_per_month', models.IntegerField(blank=True, null=True, validators=[anusha.models.validate_amount])),
                ('company_name', models.CharField(blank=True, default='', max_length=100, null=True, validators=[anusha.models.validate_only_letters])),
                ('company_type', models.CharField(blank=True, max_length=50, null=True, validators=[anusha.models.validate_only_letters])),
                ('job_joining_date', models.DateField(blank=True, null=True, validators=[anusha.models.validate_date])),
                ('job_location', models.CharField(blank=True, max_length=100, null=True)),
                ('total_job_experience', models.IntegerField(blank=True, null=True)),
                ('net_income_per_month', models.IntegerField(blank=True, null=True, validators=[anusha.models.validate_amount])),
                ('business_name', models.CharField(blank=True, max_length=100, null=True, validators=[anusha.models.validate_only_letters])),
                ('business_type', models.CharField(blank=True, max_length=50, null=True, validators=[anusha.models.validate_only_letters])),
                ('business_establishment_date', models.DateField(blank=True, null=True, validators=[anusha.models.validate_date])),
                ('gst_certificate', models.BooleanField(default=False, verbose_name='GST Certificate?')),
                ('gst_number', models.CharField(blank=True, max_length=15, null=True, validators=[anusha.models.validate_gst_number], verbose_name='GST Number')),
                ('nature_of_business', models.TextField(blank=True, null=True, validators=[anusha.models.validate_only_letters])),
                ('turnover_in_lakhs_per_year', models.IntegerField(blank=True, null=True, validators=[anusha.models.validate_amount])),
                ('property_value', models.IntegerField(validators=[anusha.models.validate_amount])),
                ('required_loan_amount', models.IntegerField(validators=[anusha.models.validate_amount])),
                ('existing_loan', models.BooleanField(default=False)),
                ('existing_loan_details', models.CharField(blank=True, max_length=100, null=True)),
                ('ref1_name', models.CharField(blank=True, max_length=100, null=True)),
                ('ref1_mobile', models.CharField(blank=True, max_length=10, null=True, validators=[anusha.models.validate_mobile_number])),
                ('ref2_name', models.CharField(blank=True, max_length=100, null=True, validators=[anusha.models.validate_only_letters])),
                ('ref2_mobile', models.CharField(blank=True, max_length=10, null=True, validators=[anusha.models.validate_mobile_number])),
                ('remarks', models.TextField(blank=True, null=True)),
                ('co_applicant_first_name', models.CharField(default='', max_length=50, validators=[anusha.models.validate_only_letters])),
                ('co_applicant_last_name', models.CharField(default='', max_length=50, validators=[anusha.models.validate_only_letters])),
                ('co_applicant_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('co_applicant_age', models.DateField(default=datetime.date(2020, 1, 1), validators=[anusha.models.validate_age])),
                ('co_applicant_relationship', models.CharField(default='', max_length=50, validators=[anusha.models.validate_only_letters])),
                ('co_applicant_mobile_number', models.CharField(default='', max_length=10, validators=[anusha.models.validate_mobile_number])),
                ('co_applicant_email_id', models.EmailField(default='@gmail.com', max_length=254, validators=[anusha.models.validate_email])),
                ('co_applicant_occupation', models.CharField(default='', max_length=50, validators=[anusha.models.validate_only_letters])),
                ('co_applicant_net_income_per_month', models.IntegerField(validators=[anusha.models.validate_amount])),
                ('random_number', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('otp', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='lapDocumentUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adhar_card_front', models.ImageField(upload_to='documents/', validators=[anusha.models.validate_image_file])),
                ('adhar_card_back', models.ImageField(upload_to='documents/', validators=[anusha.models.validate_image_file])),
                ('pan_card', models.ImageField(upload_to='documents/', validators=[anusha.models.validate_image_file])),
                ('customer_photo', models.ImageField(upload_to='documents/', validators=[anusha.models.validate_image_file])),
                ('property_photo1', models.ImageField(upload_to='documents/', validators=[anusha.models.validate_image_file])),
                ('property_photo2', models.ImageField(upload_to='documents/', validators=[anusha.models.validate_image_file])),
                ('property_photo3', models.ImageField(upload_to='documents/', validators=[anusha.models.validate_image_file])),
                ('property_photo4', models.ImageField(upload_to='documents/', validators=[anusha.models.validate_image_file])),
                ('pay_slips', models.FileField(blank=True, null=True, upload_to='documents/', validators=[anusha.models.validate_pdf_file])),
                ('bank_statement', models.FileField(blank=True, null=True, upload_to='documents/', validators=[anusha.models.validate_pdf_file])),
                ('employee_id_card', models.ImageField(blank=True, null=True, upload_to='documents/', validators=[anusha.models.validate_image_file])),
                ('business_proof1', models.FileField(blank=True, null=True, upload_to='documents/', validators=[anusha.models.validate_pdf_file])),
                ('business_proof2', models.FileField(blank=True, null=True, upload_to='documents/', validators=[anusha.models.validate_pdf_file])),
                ('bank_statement_12m', models.FileField(blank=True, null=True, upload_to='documents/', validators=[anusha.models.validate_pdf_file])),
                ('business_office_photo', models.ImageField(blank=True, null=True, upload_to='documents/', validators=[anusha.models.validate_image_file])),
                ('itr1', models.FileField(blank=True, null=True, upload_to='documents/', validators=[anusha.models.validate_pdf_file])),
                ('itr2', models.FileField(blank=True, null=True, upload_to='documents/', validators=[anusha.models.validate_pdf_file])),
                ('itr3', models.FileField(blank=True, null=True, upload_to='documents/', validators=[anusha.models.validate_pdf_file])),
                ('address_proof', models.FileField(blank=True, null=True, upload_to='documents/', validators=[anusha.models.validate_pdf_file])),
                ('existing_loan_statement', models.FileField(blank=True, null=True, upload_to='documents/', validators=[anusha.models.validate_pdf_file])),
                ('other_document1', models.FileField(blank=True, null=True, upload_to='documents/', validators=[anusha.models.validate_pdf_file])),
                ('other_document2', models.FileField(blank=True, null=True, upload_to='documents/', validators=[anusha.models.validate_pdf_file])),
                ('other_document3', models.FileField(blank=True, null=True, upload_to='documents/', validators=[anusha.models.validate_pdf_file])),
                ('other_document4', models.FileField(blank=True, null=True, upload_to='documents/', validators=[anusha.models.validate_pdf_file])),
                ('co_applicant_adhar_card_front', models.ImageField(default='image', upload_to='documents/adhar_front/', validators=[anusha.models.validate_image_file])),
                ('co_applicant_adhar_card_back', models.ImageField(default='image', upload_to='documents/adhar_back/', validators=[anusha.models.validate_image_file])),
                ('co_applicant_pan_card', models.ImageField(default='image', upload_to='documents/pan_card/', validators=[anusha.models.validate_image_file])),
                ('co_applicant_selfie_photo', models.ImageField(default='image', upload_to='documents/selfie_photo/', validators=[anusha.models.validate_image_file])),
                ('personal_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anusha.loanapplication')),
            ],
        ),
        migrations.CreateModel(
            name='lapApplicationVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_detail_verifaction', models.CharField(blank=True, max_length=50)),
                ('documents_upload_verification', models.CharField(blank=True, max_length=50)),
                ('kyc_and_document_verification', models.CharField(blank=True, max_length=50)),
                ('field_officer_visit_inspection', models.CharField(blank=True, max_length=50)),
                ('eligibility_check_verification', models.CharField(blank=True, max_length=50)),
                ('Application_fee_paid', models.CharField(blank=True, max_length=50)),
                ('tele_verification', models.CharField(blank=True, max_length=50)),
                ('bank_login_fee_paid', models.CharField(blank=True, max_length=50)),
                ('bank_login_done', models.CharField(blank=True, max_length=50)),
                ('credit_manager_visit', models.CharField(blank=True, max_length=50)),
                ('bank_or_nbfc_soft_loan_sanctioned', models.CharField(blank=True, max_length=50)),
                ('final_loan_sanctioned', models.CharField(blank=True, max_length=50)),
                ('legal_techinal_completed', models.CharField(blank=True, max_length=50)),
                ('agreement_signatures_done', models.CharField(blank=True, max_length=50)),
                ('enach_verification', models.CharField(blank=True, max_length=50)),
                ('disbursment_verification', models.CharField(blank=True, max_length=50)),
                ('post_documentation', models.CharField(blank=True, max_length=100)),
                ('cheque_issued', models.CharField(blank=True, max_length=100)),
                ('total_application_status', models.CharField(blank=True, max_length=100)),
                ('loan', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicationverification', to='anusha.loanapplication')),
            ],
        ),
    ]