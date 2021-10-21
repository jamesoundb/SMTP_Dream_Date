resource "local_file" "dream_date" {
    content     = "Tonight your random dream date animal is ${random_pet.dream_animal.id}"
    filename = "/Users/jameswurbel/SMTP_Dream_Date/tfanimal.txt"
}

resource "random_pet" "dream_animal" {
    separator = var.separator
    length = "3"
}

resource "random_string" "random" {
  length = "16"
  number = false

}

resource "random_uuid" "test" {
}

