# Maltego Entities - Maltego Chlorine 3.6.0
# Parser written by:
# Justin Seitz - justin@hunch.ly

class Unknown(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Unknown"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class Computer(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Computer"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["device"] = ""
        self.entity_attribute_names["device"] = "Device"


class DesktopComputer(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.DesktopComputer"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class Device(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Device"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["device"] = ""
        self.entity_attribute_names["device"] = "Device"


class MobileComputer(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.MobileComputer"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["device"] = ""
        self.entity_attribute_names["device"] = "Device"


class MobilePhone(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.MobilePhone"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["device"] = ""
        self.entity_attribute_names["device"] = "Device"


class Smartphone(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Smartphone"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["device"] = ""
        self.entity_attribute_names["device"] = "Device"


class Conversation(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Conversation"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["title"] = ""
        self.entity_attribute_names["title"] = "Title"
        self.entity_attributes["people"] = ""
        self.entity_attribute_names["people"] = "People"


class ConversationEmail(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.ConversationEmail"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["email"] = ""
        self.entity_attribute_names["email"] = "Sender Email"
        self.entity_attributes["email.recipients"] = ""
        self.entity_attribute_names["email.recipients"] = "Recipient Emails"


class ConversationPhone(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.ConversationPhone"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["phonenumber.caller"] = ""
        self.entity_attribute_names["phonenumber.caller"] = "Caller Number"
        self.entity_attributes["phonenumber.callee"] = ""
        self.entity_attribute_names["phonenumber.callee"] = "Callee Number"
        self.entity_attributes["starttime"] = ""
        self.entity_attribute_names["starttime"] = "Start time"
        self.entity_attributes["duration"] = ""
        self.entity_attribute_names["duration"] = "Duration"


class Event(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Event"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["title"] = ""
        self.entity_attribute_names["title"] = "Title"
        self.entity_attributes["starttime"] = ""
        self.entity_attribute_names["starttime"] = "Start Time"
        self.entity_attributes["stoptime"] = ""
        self.entity_attribute_names["stoptime"] = "Stop Time"


class Incident(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Incident"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["title"] = ""
        self.entity_attribute_names["title"] = "Title"


class Meeting(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Meeting"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["title"] = ""
        self.entity_attribute_names["title"] = "Title"
        self.entity_attributes["people"] = ""
        self.entity_attribute_names["people"] = "People"


class MeetingBusiness(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.MeetingBusiness"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class MeetingSocial(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.MeetingSocial"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class Company(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Company"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["title"] = ""
        self.entity_attribute_names["title"] = "Name"


class EducationInstitution(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.EducationInstitution"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["title"] = ""
        self.entity_attribute_names["title"] = "Name"


class Gang(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Gang"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["title"] = ""
        self.entity_attribute_names["title"] = "Name"


class OnlineGroup(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.OnlineGroup"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["title"] = ""
        self.entity_attribute_names["title"] = "Name"
        self.entity_attributes["url"] = ""
        self.entity_attribute_names["url"] = "URL"


class Organization(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Organization"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["title"] = ""
        self.entity_attribute_names["title"] = "Name"


class PoliticalMovement(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.PoliticalMovement"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["title"] = ""
        self.entity_attribute_names["title"] = "Name"


class ReligiousGroup(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.ReligiousGroup"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["title"] = ""
        self.entity_attribute_names["title"] = "Name"


class AS(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.AS"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["as.number"] = ""
        self.entity_attribute_names["as.number"] = "AS Number"


class DNSName(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.DNSName"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["fqdn"] = ""
        self.entity_attribute_names["fqdn"] = "DNS Name"


class Domain(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Domain"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["fqdn"] = ""
        self.entity_attribute_names["fqdn"] = "Domain Name"
        self.entity_attributes["whois-info"] = ""
        self.entity_attribute_names["whois-info"] = "WHOIS Info"


class IPv4Address(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.IPv4Address"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["ipv4-address"] = ""
        self.entity_attribute_names["ipv4-address"] = "IP Address"
        self.entity_attributes["ipaddress.internal"] = ""
        self.entity_attribute_names["ipaddress.internal"] = "Internal"


class MXRecord(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.MXRecord"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["fqdn"] = ""
        self.entity_attribute_names["fqdn"] = "MX Record"
        self.entity_attributes["mxrecord.priority"] = ""
        self.entity_attribute_names["mxrecord.priority"] = "Priority"


class Netblock(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Netblock"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["ipv4-range"] = ""
        self.entity_attribute_names["ipv4-range"] = "IP Range"


class NSRecord(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.NSRecord"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["fqdn"] = ""
        self.entity_attribute_names["fqdn"] = "NS Record"


class URL(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.URL"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["short-title"] = ""
        self.entity_attribute_names["short-title"] = "Short title"
        self.entity_attributes["url"] = ""
        self.entity_attribute_names["url"] = "URL"
        self.entity_attributes["title"] = ""
        self.entity_attribute_names["title"] = "Title"


class Website(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Website"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["fqdn"] = ""
        self.entity_attribute_names["fqdn"] = "Website"
        self.entity_attributes["website.ssl-enabled"] = ""
        self.entity_attribute_names["website.ssl-enabled"] = "SSL Enabled"
        self.entity_attributes["ports"] = ""
        self.entity_attribute_names["ports"] = "Ports"


class WebTitle(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.WebTitle"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["title"] = ""
        self.entity_attribute_names["title"] = "Title"


class Airport(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Airport"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["location.name"] = ""
        self.entity_attribute_names["location.name"] = "Name"


class Church(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Church"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["location.name"] = ""
        self.entity_attribute_names["location.name"] = "Name"


class CircularArea(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.CircularArea"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["area.circular"] = ""
        self.entity_attribute_names["area.circular"] = "Circular Area"
        self.entity_attributes["latitude"] = ""
        self.entity_attribute_names["latitude"] = "Latitude"
        self.entity_attributes["longitude"] = ""
        self.entity_attribute_names["longitude"] = "Longitude"
        self.entity_attributes["radius"] = ""
        self.entity_attribute_names["radius"] = "Radius (m)"


class City(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.City"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class Country(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Country"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class CrimeScene(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.CrimeScene"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class Harbor(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Harbor"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["location.name"] = ""
        self.entity_attribute_names["location.name"] = "Name"


class Home(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Home"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class Location(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Location"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["location.name"] = ""
        self.entity_attribute_names["location.name"] = "Name"
        self.entity_attributes["country"] = ""
        self.entity_attribute_names["country"] = "Country"
        self.entity_attributes["city"] = ""
        self.entity_attribute_names["city"] = "City"
        self.entity_attributes["streetaddress"] = ""
        self.entity_attribute_names["streetaddress"] = "Street Address"
        self.entity_attributes["location.area"] = ""
        self.entity_attribute_names["location.area"] = "Area"
        self.entity_attributes["location.areacode"] = ""
        self.entity_attribute_names["location.areacode"] = "Area Code"
        self.entity_attributes["countrycode"] = ""
        self.entity_attribute_names["countrycode"] = "Country Code"
        self.entity_attributes["longitude"] = ""
        self.entity_attribute_names["longitude"] = "Longitude"
        self.entity_attributes["latitude"] = ""
        self.entity_attribute_names["latitude"] = "Latitude"


class NominatimLocation(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.NominatimLocation"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["nominatimlocation"] = ""
        self.entity_attribute_names["nominatimlocation"] = "Nominatim Location"


class Office(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Office"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class Prison(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Prison"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["location.name"] = ""
        self.entity_attribute_names["location.name"] = "Name"


class Region(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Region"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["location.name"] = ""
        self.entity_attribute_names["location.name"] = "Name"


class Shop(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Shop"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["location.name"] = ""
        self.entity_attribute_names["location.name"] = "Name"


class TrainStation(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.TrainStation"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["location.name"] = ""
        self.entity_attribute_names["location.name"] = "Name"


class TransportHub(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.TransportHub"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["location.name"] = ""
        self.entity_attribute_names["location.name"] = "Name"


class BadGuy(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.BadGuy"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class BusinessLeader(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.BusinessLeader"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class Businessman(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Businessman"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class Child(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Child"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class DrugDealer(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.DrugDealer"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class Female(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Female"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["person.firstnames"] = ""
        self.entity_attribute_names["person.firstnames"] = "First Names"


class GangLeader(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.GangLeader"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class GangMember(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.GangMember"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class GoodGuy(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.GoodGuy"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class GovernmentOfficial(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.GovernmentOfficial"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class Judge(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Judge"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class LawOfficer(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.LawOfficer"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class Lawyer(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Lawyer"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class Male(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Male"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class MilitaryOfficer(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.MilitaryOfficer"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class SexOffender(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.SexOffender"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class Terrorist(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Terrorist"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class TerroristLeader(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.TerroristLeader"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class Unsub(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Unsub"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class Alias(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Alias"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["alias"] = ""
        self.entity_attribute_names["alias"] = "Alias"


class Document(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Document"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["title"] = ""
        self.entity_attribute_names["title"] = "Title"
        self.entity_attributes["document.meta-data"] = ""
        self.entity_attribute_names["document.meta-data"] = "Meta-Data"
        self.entity_attributes["url"] = ""
        self.entity_attribute_names["url"] = "URL"


class EmailAddress(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.EmailAddress"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["email"] = ""
        self.entity_attribute_names["email"] = "Email Address"


class File(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.File"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["source"] = ""
        self.entity_attribute_names["source"] = "Source"
        self.entity_attributes["description"] = ""
        self.entity_attribute_names["description"] = "Description"


class GPS(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.GPS"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["gps.coordinate"] = ""
        self.entity_attribute_names["gps.coordinate"] = "GPS Coordinate"
        self.entity_attributes["latitude"] = ""
        self.entity_attribute_names["latitude"] = "Latitude"
        self.entity_attributes["longitude"] = ""
        self.entity_attribute_names["longitude"] = "Longitude"


class Image(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Image"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["description"] = ""
        self.entity_attribute_names["description"] = "Description"
        self.entity_attributes["url"] = ""
        self.entity_attribute_names["url"] = "URL"


class Person(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Person"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["person.fullname"] = ""
        self.entity_attribute_names["person.fullname"] = "Full Name"
        self.entity_attributes["person.firstnames"] = ""
        self.entity_attribute_names["person.firstnames"] = "First Names"
        self.entity_attributes["person.lastname"] = ""
        self.entity_attribute_names["person.lastname"] = "Surname"


class PhoneNumber(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.PhoneNumber"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["phonenumber"] = ""
        self.entity_attribute_names["phonenumber"] = "Phone Number"
        self.entity_attributes["phonenumber.countrycode"] = ""
        self.entity_attribute_names["phonenumber.countrycode"] = "Country Code"
        self.entity_attributes["phonenumber.citycode"] = ""
        self.entity_attribute_names["phonenumber.citycode"] = "City Code"
        self.entity_attributes["phonenumber.areacode"] = ""
        self.entity_attribute_names["phonenumber.areacode"] = "Area Code"
        self.entity_attributes["phonenumber.lastnumbers"] = ""
        self.entity_attribute_names["phonenumber.lastnumbers"] = "Last Digits"


class PhoneNumberMobile(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.PhoneNumberMobile"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class PhoneNumberOffice(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.PhoneNumberOffice"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class PhoneNumberResidential(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.PhoneNumberResidential"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class Phrase(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Phrase"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["text"] = ""
        self.entity_attribute_names["text"] = "Text"


class Affiliation(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Affiliation"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["person.name"] = ""
        self.entity_attribute_names["person.name"] = "Name"
        self.entity_attributes["affiliation.network"] = ""
        self.entity_attribute_names["affiliation.network"] = "Network"
        self.entity_attributes["affiliation.uid"] = ""
        self.entity_attribute_names["affiliation.uid"] = "UID"
        self.entity_attributes["affiliation.profile-url"] = ""
        self.entity_attribute_names["affiliation.profile-url"] = "Profile URL"


class Facebook(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.affiliation.Facebook"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["person.name"] = ""
        self.entity_attribute_names["person.name"] = "Name"
        self.entity_attributes["affiliation.network"] = ""
        self.entity_attribute_names["affiliation.network"] = "Network"
        self.entity_attributes["affiliation.uid"] = ""
        self.entity_attribute_names["affiliation.uid"] = "UID"
        self.entity_attributes["affiliation.profile-url"] = ""
        self.entity_attribute_names["affiliation.profile-url"] = "Profile URL"


class LinkedIn(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.affiliation.LinkedIn"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["person.name"] = ""
        self.entity_attribute_names["person.name"] = "Name"
        self.entity_attributes["affiliation.network"] = ""
        self.entity_attribute_names["affiliation.network"] = "Network"


class Twitter(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.affiliation.Twitter"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["person.name"] = ""
        self.entity_attribute_names["person.name"] = "Name"
        self.entity_attributes["affiliation.network"] = ""
        self.entity_attribute_names["affiliation.network"] = "Network"
        self.entity_attributes["affiliation.uid"] = ""
        self.entity_attribute_names["affiliation.uid"] = "UID"
        self.entity_attributes["affiliation.profile-url"] = ""
        self.entity_attribute_names["affiliation.profile-url"] = "Profile URL"
        self.entity_attributes["twitter.id"] = ""
        self.entity_attribute_names["twitter.id"] = "Twitter ID"
        self.entity_attributes["twitter.screen-name"] = ""
        self.entity_attribute_names["twitter.screen-name"] = "Screen Name"
        self.entity_attributes["twitter.friendcount"] = ""
        self.entity_attribute_names["twitter.friendcount"] = "Friend Count"
        self.entity_attributes["person.fullname"] = ""
        self.entity_attribute_names["person.fullname"] = "Real Name"


class BankAccount(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.BankAccount"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["bank.accnumber"] = ""
        self.entity_attribute_names["bank.accnumber"] = "Account Number"
        self.entity_attributes["bank.name"] = ""
        self.entity_attribute_names["bank.name"] = "Bank"
        self.entity_attributes["bank.branch"] = ""
        self.entity_attribute_names["bank.branch"] = "Branch Code"


class FlightNumber(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.FlightNumber"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["flight.id"] = ""
        self.entity_attribute_names["flight.id"] = "Flight ID"
        self.entity_attributes["flight.number"] = ""
        self.entity_attribute_names["flight.number"] = "Flight Number"
        self.entity_attributes["flight.airline"] = ""
        self.entity_attribute_names["flight.airline"] = "Airline"
        self.entity_attributes["flight.date"] = ""
        self.entity_attribute_names["flight.date"] = "Date"


class IdentificationNumber(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.IdentificationNumber"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["identification.number"] = ""
        self.entity_attribute_names["identification.number"] = "Number"


class MacAddress(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.MacAddress"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["macaddress"] = ""
        self.entity_attribute_names["macaddress"] = "MAC Address"


class PassportNumber(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.PassportNumber"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        pass


class VehicleRegistration(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.VehicleRegistration"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["vehicle.registration"] = ""
        self.entity_attribute_names["vehicle.registration"] = "Registration Number"


class VinNumber(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.VinNumber"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["vinnumber"] = ""
        self.entity_attribute_names["vinnumber"] = "VIN Number"


class Bike(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Bike"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["transport.make"] = ""
        self.entity_attribute_names["transport.make"] = "Make"


class Boat(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Boat"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["transport.make"] = ""
        self.entity_attribute_names["transport.make"] = "Make"


class Bus(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Bus"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["transport.make"] = ""
        self.entity_attribute_names["transport.make"] = "Make"


class Car(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Car"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["transport.make"] = ""
        self.entity_attribute_names["transport.make"] = "Make"


class Plane(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Plane"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["transport.make"] = ""
        self.entity_attribute_names["transport.make"] = "Make"


class Train(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Train"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["transport.make"] = ""
        self.entity_attribute_names["transport.make"] = "Make"


class Transport(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Transport"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["transport.name"] = ""
        self.entity_attribute_names["transport.name"] = "Name"
        self.entity_attributes["transport.make"] = ""
        self.entity_attribute_names["transport.make"] = "Make"
        self.entity_attributes["transport.model"] = ""
        self.entity_attribute_names["transport.model"] = "Model"


class Ammunition(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Ammunition"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["weapon.type"] = ""
        self.entity_attribute_names["weapon.type"] = "Type"


class BioWeapon(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.BioWeapon"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["weapon.type"] = ""
        self.entity_attribute_names["weapon.type"] = "Type"


class Blade(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Blade"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["weapon.type"] = ""
        self.entity_attribute_names["weapon.type"] = "Type"


class ChemicalWeapon(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.ChemicalWeapon"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["weapon.type"] = ""
        self.entity_attribute_names["weapon.type"] = "Type"


class Explosive(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Explosive"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["weapon.type"] = ""
        self.entity_attribute_names["weapon.type"] = "Type"


class Gun(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Gun"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["weapon.type"] = ""
        self.entity_attribute_names["weapon.type"] = "Type"


class IED(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.IED"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["weapon.type"] = ""
        self.entity_attribute_names["weapon.type"] = "Type"


class Missile(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Missile"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["weapon.type"] = ""
        self.entity_attribute_names["weapon.type"] = "Type"


class NuclearWeapon(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.NuclearWeapon"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["weapon.type"] = ""
        self.entity_attribute_names["weapon.type"] = "Type"


class Weapon(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.Weapon"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["weapon.type"] = ""
        self.entity_attribute_names["weapon.type"] = "Type"


class WMD(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "maltego.WMD"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["weapon.type"] = ""
        self.entity_attribute_names["weapon.type"] = "Type"


class HunchlyCase(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "hunchly.HunchlyCase"
        self.entity_attributes = {}
        self.entity_attribute_names = {}
        self.entity_attributes["properties.hunchlycase"] = ""
        self.entity_attributes["case_id"] = ""
        self.entity_attribute_names['properties.hunchlycase'] = "Hunchly Case"
        self.entity_attribute_names['case_id'] = "Case ID"


class HunchlyPage(object):

    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "hunchly.HunchlyPage"
        self.entity_attributes = {"properties.hunchlypage": entity_value, "page_id": "", "url": "", "title": "",
                                  "short-title": ""}

        self.entity_attribute_names = {"properties.hunchlypage": "Hunchly Page", "page_id": "Page ID", "url": "URL",
                                       "title": "Title", "short-title": "Short Title"}


class HunchlyPhoto(object):

    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "hunchly.HunchlyPhoto"
        self.entity_attributes = {"properties.hunchlyphoto": entity_value, "url": "", "hash": "", "local_file": ""}

        self.entity_attribute_names = {"properties.hunchlyphoto": "Hunchly Page", "url": "URL", "hash": "SHA-256",
                                       "local_file": "Local File"}

class HunchlyTaggedPhoto(object):

    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "hunchly.HunchlyTaggedPhoto"
        self.entity_attributes = {"properties.hunchlyphoto": entity_value, "url": "", "hash": "", "local_file": ""}

        self.entity_attribute_names = {"properties.hunchlyphoto": "Hunchly Page", "url": "URL", "hash": "SHA-256",
                                       "local_file": "Local File"}


class HunchlySelector(object):

    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "hunchly.HunchlySelector"
        self.entity_attributes = {"properties.hunchlyselector": entity_value}

        self.entity_attribute_names = {"properties.hunchlyselector": "Hunchly Selector"}


class HunchlyData(object):
    def __init__(self, entity_value):
        self.entity_value = entity_value
        self.entity_type = "hunchly.HunchlyData"
        self.entity_attributes = {}
        self.entity_attribute_names = {}


def convert_entity(transform, entity_obj):
    new_entity = transform.addEntity(entity_obj.entity_type, entity_obj.entity_value)

    for i in entity_obj.entity_attributes:
        new_entity.addAdditionalFields(i, entity_obj.entity_attribute_names[i], False, entity_obj.entity_attributes[i])

    new_entity.setValue(entity_obj.entity_value)

    return new_entity
