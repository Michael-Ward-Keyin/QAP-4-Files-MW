var customerInfo = {
    name: `Joe Bahama`,
    birthDate: new Date(`1970-04-26`),
    gender: `Male`,
    height: `5'10"`,
    hairColour: `Brown`,
    maritalStatus: `Married`,
    roomPref: [`King Bed`, `Pet Friendly`, `Balcony`],
    paymentMethod: `Credit Card`,
    mailingAddress: {
        street:`48 Kenmount Road`,
        city: `Gander`,
        province: `NL`,
        postalCode: `A1A1A1`
    },
    phoneNumber: `7099999999`,
    bookingDates:{
    checkIn:  new Date (`2024-07-01`),
    checkOut:  new Date (`2024-07-15`),
    }, 
    };

const today = new Date();
custAge = today.getFullYear() - customerInfo.birthDate.getFullYear()

differenceMilliseconds = customerInfo.bookingDates.checkOut - customerInfo.bookingDates.checkIn;
daysMilliseconds = 1000 * 60 * 60 * 24;
stayLength = differenceMilliseconds / daysMilliseconds;
console.log(`Stay Duration: ${stayLength} days`)
console.log(`Customer Age: ${custAge}`)

html = `
    <ul>
        <li>Customer Name: ${customerInfo.name}</li>
        <li>Customer Age: ${custAge}</li>
        <li>Gender: ${customerInfo.gender}</li>
        <li>Height: ${customerInfo.height}</li>
        <li>Hair Colour: ${customerInfo.hairColour}</li>
        <li>Marital Status: ${customerInfo.maritalStatus}</li>
        <li>Room Preferences: ${customerInfo.roomPref}</li>
        <li>Payment Method: ${customerInfo.paymentMethod}</li>
        <li>Mailing Address: ${customerInfo.mailingAddress.street}, ${customerInfo.mailingAddress.city}, ${customerInfo.mailingAddress.province}, ${customerInfo.mailingAddress.postalCode}</li>
        <li>Check In: ${customerInfo.bookingDates.checkIn}</li>
        <li>Check Out: ${customerInfo.bookingDates.checkOut}</li>
        <li>Stay Duration: ${stayLength} days</li>

`;

document.body.innerHTML = html;
