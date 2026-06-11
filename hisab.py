import os
from datetime import datetime

# নোটপ্যাড ফাইলের নাম "হিসাব" রাখা হলো
FILENAME = "হিসাব.txt"

def initialize_file():
    """ফাইলটি না থাকলে 'হিসাব.txt' নামে নতুন ফাইল তৈরি করবে"""
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", encoding="utf-8") as f:
            f.write("=========================================\n")
            f.write("          অ্যাপের নাম: হিসাব (Hisab)         \n")
            f.write("         মাসিক আয়-ব্যয় ও পাওনা খাতা         \n")
            f.write("=========================================\n\n")

def write_to_notepad(category, detail, amount):
    """নোটপ্যাডে বাংলা ফরম্যাটে ডেটা লেখার ফাংশন"""
    current_time = datetime.now().strftime("%Y-%m-%d %I:%M %p")
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(f"[{current_time}] | {category} | {detail}: {amount} টাকা\n")
    print(f"\n✅ সফলতা: আপনার তথ্যটি '{FILENAME}' ফাইলে যোগ করা হয়েছে!")

def main_menu():
    initialize_file()
    
    while True:
        print("\n=== অ্যাপ: হিসাব ===")
        print("১. মাসিক আয় (Income) যোগ করুন")
        print("২. মাসিক ব্যয় (Expense) যোগ করুন")
        print("৩. টাকা প্রদানকারীদের আলাদা হিসাব (কার থেকে পেলেন)")
        print("৪. 'হিসাব.txt' ফাইলটি এখানেই দেখুন")
        print("৫. অ্যাপ বন্ধ করুন")
        
        choice = input("\nআপনার পছন্দ সিলেক্ট করুন (১-৫): ")
        
        if choice == '১':
            detail = input("আয়ের উৎস বা বিবরণ (যেমন: বেতন, পার্ট-টাইম কাজ): ")
            amount = input("টাকার পরিমাণ: ")
            write_to_notepad("মাসিক আয়", detail, amount)
            
        elif choice == '২':
            detail = input("ব্যয়ের খাত বা বিবরণ (যেমন: বাড়ি ভাড়া, বাজার খরচ): ")
            amount = input("টাকার পরিমাণ: ")
            write_to_notepad("মাসিক ব্যয়", detail, amount)
            
        elif choice == '৩':
            person_name = input("যিনি টাকা দিয়েছেন তার নাম: ")
            reason = input("কী বাবদ টাকা দিলেন (যেমন: টিউশনি ফি, ধার ফেরত, উপহার): ")
            amount = input("টাকার পরিমাণ: ")
            detail = f"প্রদানকারী: {person_name} ({reason})"
            write_to_notepad("টাকা প্রাপ্তি", detail, amount)
            
        elif choice == '৪':
            print(f"\n--- বর্তমানে '{FILENAME}' ফাইলের ভেতরে যা আছে ---")
            if os.path.exists(FILENAME):
                with open(FILENAME, "r", encoding="utf-8") as f:
                    print(f.read())
            else:
                print("এখনো কোনো হিসাব লেখা হয়নি।")
            print("------------------------------------------------")
            
        elif choice == '৫':
            print("\n'হিসাব' অ্যাপটি বন্ধ হচ্ছে। ভালো থাকুন!")
            break
        else:
            print("\n❌ ভুল অপশন! দয়া করে ১ থেকে ৫ এর মধ্যে সঠিক সংখ্যাটি চাপুন।")

if _name_ == "_main_":
    main_menu(