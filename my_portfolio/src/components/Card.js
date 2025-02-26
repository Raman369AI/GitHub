import React from "react";
import {
  Heading,
  HStack,
  Image,
  Text,
  VStack,
  Box,
  Link,
  Button,
  useDisclosure,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalCloseButton,
  ModalBody,
  ListItem,
  OrderedList
} from "@chakra-ui/react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowRight, faCode } from "@fortawesome/free-solid-svg-icons";
import { motion } from "framer-motion";

const AnimatedBox = motion(Box);

const Card = ({ title, description, imageSrc, url }) => {
  const { isOpen, onOpen, onClose } = useDisclosure();

  return (
    <AnimatedBox
      p={4}
      bg="white"
      color="black"
      borderRadius="xl"
      whileHover={{ scale: 1.05, boxShadow: "0px 4px 8px rgba(0, 0, 0, 0.2)" }}
      transition={{ duration: 0.3 }}
      style={{ height: "100%" }}
    >
      <VStack spacing={4} h="100%" justifyContent="space-between">
        <Image src={imageSrc} alt={title} borderRadius="xl" objectFit="cover" />
        <VStack alignItems="flex-start" spacing={2} h="100%">
          <Heading as="h3" size="md">
            {title}
          </Heading>
          <Box>
            {/* Render description as ordered list */}
            <Text color="#64748b" display={{ base: "block", md: "none" }}>
              {/* Display the modal in mobile view */}
              <Button colorScheme="purple" size="sm" onClick={onOpen}>
                Read More
              </Button>
            </Text>
            <OrderedList
              pl={5}
              spacing={1}
              display={{ base: "none", md: "block" }}
            >
              {description.map((item, idx) => (
                <ListItem key={idx} color="#64748b">
                  {item}
                </ListItem>
              ))}
            </OrderedList>
          </Box>
          <HStack spacing={4} mt={4}>
            {url && (
              <Link href={url} isExternal>
                <Button
                  leftIcon={<FontAwesomeIcon icon={faCode} />}
                  colorScheme="purple"
                  size="sm"
                >
                  GitHub
                </Button>
              </Link>
            )}
            <Box display={{ base: "none", md: "block" }}>
              {" "}
              {/* Display the modal in desktop view */}
              <Button colorScheme="purple" size="sm" onClick={onOpen}>
                Read More
              </Button>
            </Box>
          </HStack>
        </VStack>
      </VStack>

      {/* Modal for Full Description */}
      <Modal isOpen={isOpen} onClose={onClose} size="xl">
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>{title}</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            <OrderedList pl={5} spacing={1}>
              {description.map((item, idx) => (
                <ListItem key={idx}>{item}</ListItem>
              ))}
            </OrderedList>
          </ModalBody>
        </ModalContent>
      </Modal>
    </AnimatedBox>
  );
};

export default Card;
